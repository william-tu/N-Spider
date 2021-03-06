# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import logging

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    data_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    message_url = scrapy.Field()
    image_url = scrapy.Field()
    add_time = scrapy.Field()
    source_from = scrapy.Field()


class GuokeItem(scrapy.Item):
    data_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    message_url = scrapy.Field()
    image_url = scrapy.Field()
    add_time = scrapy.Field()
    source_from = scrapy.Field()


class ZhihuItem(scrapy.Item):
    data_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    message_url = scrapy.Field()
    image_url = scrapy.Field()
    add_time = scrapy.Field()
    source_from = scrapy.Field()


class GuinessItem(scrapy.Item):
    data_id = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    message_url = scrapy.Field()
    add_time = scrapy.Field()
    image_url = scrapy.Field()
    source_from = scrapy.Field()