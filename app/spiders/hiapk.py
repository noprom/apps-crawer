# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from app.items import HiapkItem

class HiapkSpider(CrawlSpider):
    name = "hiapk"
    allowed_domains = ["hiapk.com"]
    start_urls = [
        'http://apk.hiapk.com/apps',
    	'http://apk.hiapk.com/apps/Social',
    	'http://apk.hiapk.com/apps/Education',
    	'http://apk.hiapk.com/apps/Finance',
    	'http://apk.hiapk.com/apps/Productivity',
    	'http://apk.hiapk.com/apps/Productivity?sort=5&pi=7'
    ]

    rules = [
        Rule(LinkExtractor(allow=("http://apk\.hiapk\.com/appinfo/", )), callback='parse_app',follow=True),
        Rule(LinkExtractor(allow=("http://apk\.hiapk\.com/apps?sort=\d+&pi=\d+", )), callback='parse',follow=True),
        Rule(LinkExtractor(allow=("http://apk\.hiapk\.com/apps", )), callback='parse',follow=True),
    ]

    def parse_app(self, response):
        item = HiapkItem()
        item['url'] = response.url
        item['app_name'] = response.css("#appSoftName").xpath("text()").extract()[0]
        item['developer'] = response.xpath("//div[@class='d_u_line']").xpath("text()").extract()
        item['package'] = response.url.split("/")[-2]
        item['category'] = response.xpath("//a[@id='categoryLink']").xpath("text()").extract()
        yield item