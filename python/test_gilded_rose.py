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
        print()
        for ii in range(40):
            gilded_rose_prec = deepcopy(gilded_rose)
            gilded_rose.update_quality()
            print(gilded_rose_prec, gilded_rose)
            sell_in, quality = item.sell_in, item.quality
            gilded_rose.update_quality()
            if sell_in > 0:
                self.assertEqual(min(quality + 1, 50), item.quality)
            else:
                self.assertEqual(min(quality + 2, 50), item.quality)

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

    # - "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 5)]
        gilded_rose = GildedRose(items)
        print()
        for ii in range(10):
            gilded_rose_prec = deepcopy(gilded_rose)
            gilded_rose.update_quality()
            for prec, cur in zip(gilded_rose_prec.items, gilded_rose.items):
                self.assertEqual(prec.quality, cur.quality)
                self.assertEqual(prec.sell_in, cur.sell_in)
            print(gilded_rose_prec, gilded_rose)

    # - "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
    def test_backstages(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 5)]
        gilded_rose = GildedRose(items)
        print()
        for ii in range(20):
            gilded_rose_prec = deepcopy(gilded_rose)
            gilded_rose.update_quality()
            print(gilded_rose_prec, gilded_rose)
            for prec, cur in zip(gilded_rose_prec.items, gilded_rose.items):
                if prec.sell_in > 10:
                    self.assertEqual(prec.quality + 1, cur.quality)
                elif prec.sell_in > 5:
                    self.assertEqual(prec.quality + 2, cur.quality)
                elif prec.sell_in > 0:
                    self.assertEqual(prec.quality + 3, cur.quality)
                else:
                    self.assertEqual(cur.quality, 0)

    #  - "Conjured" items degrade in Quality twice as fast as normal item
    def test_conjured(self):
        items = [Item("Conjured", 5, 5)]
        gilded_rose = GildedRose(items)
        print()
        for ii in range(10):
            gilded_rose_prec = deepcopy(gilded_rose)
            gilded_rose.update_quality()
            for prec, cur in zip(gilded_rose_prec.items, gilded_rose.items):
                if prec.sell_in > 0:
                    self.assertEqual(max(prec.quality - 2, 0), cur.quality)
                else:
                    self.assertEqual(max(prec.quality - 4, 0), cur.quality)
            print(gilded_rose_prec, gilded_rose)
            # print(item)


if __name__ == "__main__":
    unittest.main()
