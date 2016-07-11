# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from app.items import GoogleItem
from scrapy.http.request import Request

class GooglePlaySpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["play.google.com"]
    start_urls = (
        'https://play.google.com/store',
        'https://play.google.com/store/apps/details?id=com.instagram.android'
    )

    rules = (
        Rule(LinkExtractor(allow=("https://play\.google\.com/store/apps/details?id=.+", )), callback='parse',follow=True),
        # Rule(LinkExtractor(allow=['/tor/\d+']), 'parse_torrent')
    ) #  CrawlSpider 会根据 rules 规则爬取页面并调用函数进行处理

    def parse(self, response):
        # for sel in response.xpath('//ul/li'):
            item = GoogleItem()
            item['url'] = response.url
            item['app_name'] = response.xpath("//div[@class='id-app-title']").xpath("text()").extract()
            item['package'] = response.url.split("id=")[-1]
            item['developer'] =  response.xpath("//span[@itemprop='name']").xpath("text()").extract()
            item['category'] = response.xpath("//span[@itemprop='genre']").xpath("text()").extract()
            # print item
            yield item