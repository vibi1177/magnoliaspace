# -*- coding: utf-8 -*-
import scrapy


class MagnoliaspaceSpider(scrapy.Spider):
    name = "magnoliaspace"
    allowed_domains = ["www.magnoliaspace.it"]
    start_urls = [
        'https://www.magnoliaspace.it/',
    ]

    def parse(self, response):
        yield{'title' : response.css('title::text').extract_first()}

