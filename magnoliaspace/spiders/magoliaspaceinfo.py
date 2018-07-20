# -*- coding: utf-8 -*-
import scrapy


class MagnoliaspaceinfoSpider(scrapy.Spider):
    name = "magnoliaspaceinfo"
    allowed_domains = ["www.magnoliaspace.it"]
    start_urls = [
        'https://www.magnoliaspace.it/mail/contatti.htm',
    ]

    def parse(self, response):
        item  = {}
        item['title'] = response.css('title::text').extract_first()
        divcol = response.xpath(
            '//div[@class="col50 contact"]'
        )
        for elem in divcol:
            item['row1'] = elem.xpath(
            './/div[@class="tit"]/text()'
            ).extract_first()
            item['row2'] =  elem.xpath(
            './/div[@class="tit"]/p/text()'
            ).extract()
        yield item