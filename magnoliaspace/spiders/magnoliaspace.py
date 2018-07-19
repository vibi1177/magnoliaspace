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
            '//div[@class="coldx"]/div[@class="contprod"]/span/div[@class="s-prod"]'
        )
        #dati = {}
        #dati['pr_urls']=[]
        #for prod in prspan:
            #dati['pr_urls'].append(prod.xpath('.//div[@class="contfoto"]/a/@href').extract_first())
        #yield dati
        for prod in prspan:
            linktoprod = prod.xpath('.//div[@class="contfoto"]/a/@href').extract_first()
            yield scrapy.Request(response.urljoin(linktoprod), callback=self.parse_prdetail)

    def parse_prdetail(self, response):
        item = {}

        item['photo'] = response.urljoin(response.xpath(
            '//div[@class="foto"]/a/@href'
        ).extract_first())
        item['category'] = response.xpath(
            '//div[@class="section"]/text()]"'
        ).extract_first()
        item['productname'] = response.xpath(
            '//div[@class="tit]/text()"'
        ).extract_first()
        item['sku'] = response.xpath(
            '//div[@class="cod]/text()"'
        ).extract_first()
        item['prdescription'] = response.xpath(
            '//div[@class="tabbing"]/div[@class="s-tab"]/div[@class="content"]/p/text()"'
        ).extract()
        yield item


