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
        'https://play.google.com/store/apps/details?id=com.viber.voip'
    )

    rules = [
        Rule(LinkExtractor(allow=("https://play\.google\.com/store/apps/details", )), callback='parse',follow=True),
    ] #  CrawlSpider 会根据 rules 规则爬取页面并调用函数进行处理

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url, cookies={
    #             # play.google.com
    #             '_ga': 'GA1.3.924697409.1462264323',
    #             '_gat': 1,
    #             'PLAY_ACTIVE_ACCOUNT': 'ICrt_XL61NBE_S0rhk8RpG0k65e0XwQVdDlvB6kxiQ8=tyeenoprom@gmail.com',
    #             'PLAY_PREFS': 'CsoECISgtsbsCBLABAoCTkwQxNbZxd0qGoUEERITFBUWGNQB1QGvAsQE4wXlBegF1wbYBt4G3waQlYEGkZWBBpKVgQaVlYEGl5WBBqSVgQa4lYEGvJWBBsCVgQbBlYEGxJWBBsWVgQbIlYEGzpWBBs-VgQbQlYEG1JWBBtmVgQbdlYEG8pWBBviVgQb5lYEGhpaBBomWgQaMloEGj5aBBpKWgQabloEGnpaBBp-WgQagloEGoZaBBqiWgQaqloEGq5aBBsqXgQbul4EG75eBBoWYgQaGmIEGvpiBBq2bgQbLm4EGvJ2BBt2dgQbnnYEGkJ6BBpaegQakoIEG7qGBBvGhgQbiooEG86KBBveigQaLo4EGmqSBBrKkgQavpYEG6qWBBv6lgQadpoEGxqaBBqOogQbEqIEGo6mBBrysgQbBr4EG1q-BBquygQassoEGvLKBBtaygQbQs4EGh7SBBrG0gQbWuYEG6LmBBvi5gQbOuoEG67qBBuy6gQbvuoEG8LqBBo7AgQaiwIEGwMCBBvLAgQaEwYEGs8KBBtbCgQbKxoEGsceBBq3JgQaeyoEG68qBBtzMgQaCzYEGh86BBrDPgQa9z4EGvs-BBvPPgQbn0IEGstGBBq_SgQbE0oEGh9OBBpXTgQaX1YEG2NaBBorXgQaT14EGwNeBBvfXgQb414EGotiBBvXYgQaJ2YEGx9uBBsfdgQaB34EGiN-BBiixlJe-3So6JDM5ODA1NDM3LTBiNTgtNDI2OC1iNGY1LTZjNzg1ZTI3MzBjMQr3AggAEvICCgJOTBD67vrF3SoatwIREhMUFdQB1QGnAsQE4wXlBegF1wbYBt4G3waQlYEGkZWBBpKVgQaXlYEGuJWBBryVgQa9lYEGwJWBBsGVgQbElYEG1JWBBtmVgQbylYEG-JWBBpuWgQadloEGnpaBBp-WgQagloEG7peBBoWYgQa-mIEGiZuBBq2bgQbLm4EGvJ2BBt2dgQbnnYEGkJ6BBqSggQbiooEG86KBBveigQaLo4EGmqSBBq-lgQbqpYEG_qWBBsamgQajqIEGxKiBBs6ogQajqYEGvKyBBtavgQarsoEGrLKBBtaygQbQs4EGsbSBBta5gQbouYEG-LmBBs66gQbruoEG7LqBBu-6gQbwuoEGosCBBsDAgQbywIEG1sKBBsrGgQaxx4EGrcmBBp7KgQbczIEGsM-BBrLRgQbE0oEGldOBBiiB7_rF3So6JDRjMjY2MDAxLWE1YzEtNDQxZi1hYzFmLWI3NGI4NmIwZGEzYg:S:ANO1ljLcr935eYediw',
    #             # google.com
    #             'APISID': 'RXo7Yo-wsYX-ZHo7/AWFyAePqKSSberb6g',
    #             'CONSENT': 'YES+LT.zh-CN+V3',
    #             'HSID': 'AWQWypeaKfQownNMj',
    #             'NID': '81=xqX8ZHj14bSZbAzFpAEjUsVDtSW9tsk8iRdJAWeF0v-BYkTMn2e1rnY8gSgydewVZgedS1E3xUtS11x7P2wvWSHh_ZxZk2H3ZSsN68tB2h1YDogXKXcIk-2Idn8OxLMOY5YFtZPMxW7QqXXZ4wRmK_mmls1UfJ6PEuAVWdgpUsjn-Av8jQDGfgscA4ATZIFJ9zfLVmEeXRRKkP7sVdvn3MO2nRZSvbbx6s4kcfGMwkIuUeLrypF56XEML2UCqo1aSAxMfUHLjcRkrDOifl-j_SbntjSjVsmMKMYT8KP31mFdvF8SfX0K3jrq',
    #             'S': 'billing-ui-v3=ggOMzlc2DtqTh3Lzx9ERYg:billing-ui-v3-efe=ggOMzlc2DtqTh3Lzx9ERYg',
    #             'SAPISID': '-9BxBneCQYGZahpK/AzB9XmIqmPxw3fvBj',
    #             'SID': 'gQMEkLApBgZwx9KsuSD6qH6HUl_2QEl_ouh-Zd9runcRr5oTszBZcc2dTPp-DP0BmiRvMQ.',
    #             'SSID': 'A0HEqpTiosVsdnUoT'
    #         })

    def parse(self, response):
        # 获取页面的 URL 以及下载数量
    	item = GoogleItem()
        item['url'] = response.url
        item['app_name'] = response.xpath("//div[@class='id-app-title']").xpath("text()").extract()
        item['package'] = response.url.split("id=")[-1]
        item['developer'] =  response.xpath("//span[@itemprop='name']").xpath("text()").extract()
        item['category'] = response.xpath("//span[@itemprop='genre']").xpath("text()").extract()
        print item
        yield item