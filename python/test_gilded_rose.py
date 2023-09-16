# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from copy import deepcopy


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    # 	- Once the sell by date has passed, Quality degrades twice as fast
    #   - The Quality of an item is never negative
    def test_rule_1_and_2(self):
        items = [Item("foo", 3, 10)]
        gilded_rose = GildedRose(items)
        print()
        for ii in range(10):
            gilded_rose_prec = deepcopy(gilded_rose)
            gilded_rose.update_quality()
            for prec, cur in zip(gilded_rose_prec.items, gilded_rose.items):
                if prec.sell_in > 0:
                    self.assertEqual(prec.quality - 1, cur.quality)
                else:
                    self.assertEqual(max(prec.quality - 2, 0), cur.quality)
            print(gilded_rose_prec, gilded_rose)
            # print(item)

    # - "Aged Brie" actually increases in Quality the older it gets
    def test_aged_brie(self):
        items = [Item("Aged Brie", 5, 0)]
        gilded_rose = GildedRose(items)
        print()
        item = items[0]
        for ii in range(40):
            sell_in, quality = item.sell_in, item.quality
            gilded_rose.update_quality()
            if sell_in > 0:
                self.assertEqual(min(quality + 1, 50), item.quality)
            else:
                self.assertEqual(min(quality + 2, 50), item.quality)
            print(item)

    #  - The Quality of an item is never more than 50
    def test_limit_50(self):
        items = [Item("Aged Brie", 5, 45)]
        gilded_rose = GildedRose(items)
        print()
        item = items[0]
        for ii in range(10):
            gilded_rose.update_quality()
            self.assertLessEqual(item.quality, 50)
            print(item)


if __name__ == "__main__":
    unittest.main()
