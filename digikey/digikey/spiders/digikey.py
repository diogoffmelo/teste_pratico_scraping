# -*- coding: utf-8 -*-
import scrapy

class DigikeySpider(scrapy.Spider):

	#spider`s name
	name = "digikey"
	
	#define scope
	allowed_domains = ["digikey.com"]
	

	#initial request
	start_urls = ["https://www.digikey.com/MyDigiKey/Login"]

	#products url base search
	search_url = "http://www.digikey.com/products/en/development-boards-kits-programmers/evaluation-boards-embedded-mcu-dsp/786"

	def parse(self, response):
		self.logger.info("Starting")
		return scrapy.Request(response.xpath("//iframe//@src").extract_first(), callback=self.parse_login_form)


	def parse_login_form(self, response):
		return scrapy.FormRequest.from_response(
			response, 
			formdata={'username': 'spiderbot', 'password': 'spiderbot'}, 
			callback=self.after_login)

	def after_login (self, response):
		self.logger.info("Logged")
		return scrapy.Request(DigikeySpider.search_url, self.search_products)

	def search_products(self, response):

		#select product links
		links = response.xpath("//tr[contains(@itemtype,'http://schema.org/Product')]//td[contains(@class, 'tr-dkPartNumber nowrap-culture')]/a/@href")

		self.logger.info("search hit {0}".format(response.url))

		for link in links:
			#rebuild full html path
			target_url = u"http://www.digikey.com{0}".format(link.extract())
		
			#create a new request to proccess the product
			yield scrapy.Request(url=target_url, callback=self.parse_product)
			
	
		#next page
		next_page = u"http://www.digikey.com{0}".format(response.xpath("//a[contains(@class, 'Next')]/@href").extract_first())
		
		if next_page:
			yield scrapy.Request(url=next_page, callback=self.search_products)
	
	#help function
	def extract_normalized(self, node, xpath_str):
		return	node.xpath("normalize-space({0})".format(xpath_str)).extract_first()
			
	def parse_product(self, response):
		#self.logger.info("product hit {0}".format(response.url))
		
		product_table_desc = response.xpath("//table[contains(@id, 'product-details')]")
		
		product = dict()
		
		product["url"] = response.url
		
		product["manufacturer"] = self.extract_normalized(product_table_desc, "//tr[./th[text()='Manufacturer']]//a//text()")
		
		product["manufacturer_link"] = u"http://www.digikey.com{0}".format(product_table_desc.xpath("//tr[./th[text()='Manufacturer']]//a/@href").extract_first())

		product["desc"] = self.extract_normalized(product_table_desc, "//tr[./th[text()='Expanded Description']]/td/text()")

		product["price"] = self.extract_normalized(response, "//span[contains(@itemprop, 'price')]/text()")
		
		#self.logger.info(product)

		#Send on pipeline
		yield product



