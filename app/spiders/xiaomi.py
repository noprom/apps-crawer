# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from app.items import XiaomiItem
from scrapy.http.request import Request

class XiaomiSpider(scrapy.Spider):
    name = "xiaomi"
    allowed_domains = ["app.xiaomi.com"]
    start_urls = (
        'http://app.xiaomi.com/',
        'http://app.xiaomi.com/category/5',
        'http://app.xiaomi.com/details?id=com.jxch.lianjiangquan'
    )

    rules = (
        Rule(LinkExtractor(allow=("http://app\.xiaomi\.com/details?id=.+", )), callback='parse',follow=True),

    ) #  CrawlSpider 会根据 rules 规则爬取页面并调用函数进行处理

    def parse(self, response):
        item = XiaomiItem()
        item['url'] = response.url
        item['app_name'] = response.xpath("//div[@class='intro-titles']/h3").xpath("text()").extract()
        item['package'] = response.url.split("id=")[-1]
        item['developer'] =  response.xpath("//div[@class='intro-titles']/p[1]").xpath("text()").extract()
        item['category'] = response.xpath("//div[@class='intro-titles']/p[2]").xpath("text()").extract()
        # print item
        yield item