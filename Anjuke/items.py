# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class AnjukeSZItem(scrapy.Item):
    bd_name = scrapy.Field()
    bd_location = scrapy.Field()
    bd_buildTime = scrapy.Field()
    bd_type = scrapy.Field()
    bd_property = scrapy.Field()
    bd_layout = scrapy.Field()
    bd_size = scrapy.Field()
    bd_direction = scrapy.Field()
    bd_floor = scrapy.Field()
    bd_lift = scrapy.Field()
    bd_averagePrice = scrapy.Field()
    bd_totalPrice = scrapy.Field()
    bd_oneHand = scrapy.Field()
    bd_decoration = scrapy.Field()
    bd_url = scrapy.Field()