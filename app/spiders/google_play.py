# -*- coding: utf-8 -*-
import scrapy


class GooglePlaySpider(scrapy.Spider):
    name = "google-play"
    allowed_domains = ["play.google.com"]
    start_urls = (
        'http://www.play.google.com/',
    )

    def parse(self, response):
        pass
