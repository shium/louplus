# -*- coding: utf-8-*-
import scrapy
import re

class Shiyanlou_Github_Spider(scrapy.Spider):
    name = 'Shiyanlou_Github_Spider'

    def start_requests(self):
        url_temp = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url_temp.format(i) for i in range(1,5))
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        for course in response.xpath('//ul[@data-filterable-for="your-repos-filter"]/li'):
            yield {
                    'name' :  course.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('\n\s*(.*)'),
                    'update_time' : course.xpath('.//relative-time/@datetime').extract_first()
                    }
