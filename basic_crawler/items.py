# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BasicCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() # data model or things for crawl
    email = scrapy.Field()
    comments = scrapy.Field()
    form = scrapy.Field()
    location_url = scrapy.Field()
