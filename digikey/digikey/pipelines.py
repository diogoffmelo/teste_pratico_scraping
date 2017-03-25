# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
from pymongo import MongoClient


class DigikeyPipeline(object):

	@classmethod
	def from_crawler(cls, crawler):

		settings = crawler.settings

		client = MongoClient(settings["connection"])
		data_base = client["data_base"]
		data_set = data_base["collection"]

		instance = DigikeyPipeline({"data_set":data_set})

		return instance

	def __init__(self, db_settings):
		self.logger = logging.getLogger(__name__)
		self.data_set = db_settings["data_set"]
	
	def process_item(self,prod, spider):
		
		prod_id = self.data_set.insert_one(prod).inserted_id
		
		if prod_id:
			self.logger.info("added {0} to database".format(prod_id))
		else:
			self.logger.info("an error ocurred while accessing the database")
				
		return prod
