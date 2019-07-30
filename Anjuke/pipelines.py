# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json

class AnjukePipeline_ToCSV(object):
    def __init__(self):
        self.f = open("anjuke.csv", "a", newline="")
        self.fieldnames = ["bd_name", "bd_location", "bd_buildTime", "bd_type", "bd_property", "bd_layout", "bd_size", "bd_direction", "bd_floor", "bd_lift", "bd_averagePrice", "bd_totalPrice", "bd_oneHand", "bd_decoration", "bd_url"]
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.f.close()


#class AnjukePipeline_ToJSON(object):
#    def __init__(self):
#        self.f = open('./anjuke.json', 'w')
#
#    def process_item(self, item, spider):
#        content = json.dumps(dict(item), ensure_ascii=False) + ","
#        self.f.write(content)
#        return item
#
#    def close_spider(self, spider):
#        self.f.close()
