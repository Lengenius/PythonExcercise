# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    # tag = scrapy.Field()
    info_array = scrapy.Field()
    read = scrapy.Field()
    reading = scrapy.Field()
    want_read = scrapy.Field()
    notes_number =scrapy.Field()
    commits_long =scrapy.Field()
    commits_short =scrapy.Field()
    rates =scrapy.Field()
    rating_people = scrapy.Field()
    authors = scrapy.Field()