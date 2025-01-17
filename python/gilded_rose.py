# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                break

            quality_increment = -1
            if item.sell_in <= 0:
                quality_increment *= 2
            if item.name == "Conjured":
                quality_increment *= 2
            if item.name in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
                quality_increment *= -1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 10:
                    quality_increment += 1
                if item.sell_in <= 5:
                    quality_increment += 1
                if item.sell_in <= 0:
                    quality_increment = 0
                    item.quality = 0

            item.quality += quality_increment
            item.sell_in = item.sell_in - 1

            if item.quality < 0:
                item.quality = 0
            if item.quality > 50:
                item.quality = 50

    def __repr__(self):
        return "\n".join([item.__repr__() for item in self.items])


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
