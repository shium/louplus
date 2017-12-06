# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import GithubItem
from datetime import datetime

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']

    def parse(self, response):
        for course in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            time_str = course.xpath('.//div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
            item = GithubItem({
                'name' : course.xpath('.//div[@class="d-inline-block mb-1"]/h3/a/text()').re_first('\n\s*(.*)'),
                'update_time' : datetime.strptime(time_str,'%Y-%m-%dT%H:%M:%SZ')
                })
            yield item

    @property
    def start_urls(self):
        url_root = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_root.format(i) for i in range(1,5))

