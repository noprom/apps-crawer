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
        'http://app.xiaomi.com/category/1',
        'http://app.xiaomi.com/category/2',
        'http://app.xiaomi.com/category/3',
        'http://app.xiaomi.com/category/4',
        'http://app.xiaomi.com/category/5',
        'http://app.xiaomi.com/category/6',
        'http://app.xiaomi.com/category/7',
        'http://app.xiaomi.com/category/8',
        'http://app.xiaomi.com/category/9',
        'http://app.xiaomi.com/category/10',
        'http://app.xiaomi.com/category/11',
        'http://app.xiaomi.com/category/12',
        'http://app.xiaomi.com/category/13',
        'http://app.xiaomi.com/category/14',
        'http://app.xiaomi.com/category/15',
        'http://app.xiaomi.com/category/16',
        'http://app.xiaomi.com/category/17',
        'http://app.xiaomi.com/category/18',
        'http://app.xiaomi.com/category/19',
        'http://app.xiaomi.com/category/20',
        'http://app.xiaomi.com/category/21',
        'http://app.xiaomi.com/category/22',
        'http://app.xiaomi.com/category/23',
        'http://app.xiaomi.com/category/24',
        'http://app.xiaomi.com/category/25',
        'http://app.xiaomi.com/category/26',
        'http://app.xiaomi.com/category/27',
        'http://app.xiaomi.com/category/28',
        'http://app.xiaomi.com/category/29',
        'http://app.xiaomi.com/category/30',
        'http://app.xiaomi.com/category/5#page=1',
        'http://app.xiaomi.com/details?id=com.jxch.lianjiangquan'
    )

    rules = (
        Rule(LinkExtractor(allow=("http://app\.xiaomi\.com/details?id=.+", )), callback='parse_app',follow=True),
        # Rule(LinkExtractor(allow=("http://app\.xiaomi\.com/", )), callback='parse',follow=True),
        # Rule(LinkExtractor(allow=("http://app\.xiaomi\.com/category/", )), callback='parse',follow=True),
        # Rule(LinkExtractor(allow=("http://app\.xiaomi\.com/category/\d+#page=\d+", )), callback='parse',follow=True),
    ) #  CrawlSpider 会根据 rules 规则爬取页面并调用函数进行处理

    # def parse(self, response):
    #     item = XiaomiItem()
    #     yield item

    def parse_app(self, response):
        item = XiaomiItem()
        item['url'] = response.url
        item['app_name'] = response.xpath("//div[@class='intro-titles']/h3").xpath("text()").extract()
        item['package'] = response.url.split("id=")[-1]
        item['developer'] =  response.xpath("//div[@class='intro-titles']/p[1]").xpath("text()").extract()
        item['category'] = response.xpath("//div[@class='bread-crumb']/ul/li[2]/a").xpath("text()").extract()
        print(item)
        yield item