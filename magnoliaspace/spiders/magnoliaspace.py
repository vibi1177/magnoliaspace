# -*- coding: utf-8 -*-
import scrapy


class MagnoliaspaceSpider(scrapy.Spider):
    name = "magnoliaspace"
    allowed_domains = ["www.magnoliaspace.it"]
    start_urls = [
        'https://www.magnoliaspace.it/catalog/section/38/i-prodotti.htm',
    ]

    def parse(self, response):
        prspan = response.xpath(
            '//div[@class="coldx"]/div[@class="contprod"]/div[@class="contcategory"]/span/div[@class="s-prod"]'
        )
        for prod in prspan:
            linktoprod = prod.xpath('.//div[@class="contfoto"]/a/@href').extract_first()
            #yield scrapy.Request(response.urljoin(linktoprod), callback=self.parse_prdetail)
            yield linktoprod


