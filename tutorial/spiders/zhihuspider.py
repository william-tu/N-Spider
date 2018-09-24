# -*- coding: utf-8 -*-
import urlparse
from datetime import datetime

import scrapy
from lxml import etree
from scrapy import signals
from scrapy_redis.spiders import RedisCrawlSpider

from ..items import ZhihuItem
from ..tools.common import get_md5


class ZhihuSpider(RedisCrawlSpider):
    '''
    redis-cli lpush zhihu:start_urls 'http://daily.zhihu.com'
    '''
    name = 'zhihu'
    allowed_domains = ['daily.zhihu.com']
    start_urls = [
        'http://daily.zhihu.com'
    ]

    def __init__(self, *args, **kwargs):
        super(ZhihuSpider, self).__init__(*args, **kwargs)

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(ZhihuSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        print 'zhihu closed'

    def parse(self, response):
        message = response.xpath('//div[@class="wrap"]').extract()
        for m in message:
            selector = etree.HTML(m)
            yield scrapy.Request(url=urlparse.urljoin(response.url, response.url + selector.xpath('//a/@href')[0]),
                                 callback=self.parse_content)

    def parse_content(self, response):
        l = ZhihuItem()
        l['title'] = response.xpath('//h1[@class="headline-title"]/text()').extract()[0]
        l['message_url'] = response.url
        l['data_id'] = get_md5(l['message_url'])
        l['image_url'] = response.xpath('//div[@class="img-wrap"]/img/@src').extract()[0]
        l['add_time'] = datetime.now()
        l['source_from'] = u'知乎日报网'
        content = ''.join(response.xpath('//div[@class="content"]/p/text()').extract())
        l['content'] = content

        yield l
