# -*- coding: utf-8 -*-

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from ncbtmb_spider.items import *

class DuplicatePipeline(object):
#    def open_spider(self, spider):
#        pass
    def __init__(self):
        self.ids_seen = []
    def process_item(self, item, spider):
        if item['Name'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.append(item['Name'])
            return item
    #def close_spider(self, spider):
    #    pass


# class DuplicatePipeline(object):

# 	def open_spider(self, spider):
# 		pass
# 	def __init__(self):
# 		self.ids_seen = set()
# 	def process_item(self, item, spider):
#         if item['Name'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else:
#             self.ids_seen.add(item['Name'])
#             return item
#     def close_spider(self, spider):
#         pass
