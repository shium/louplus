# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import GithubItem
from datetime import datetime

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']

    def parse(self, response):
        item = GithubItem()
        for course in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            time_str = course.xpath('.//div[@class="f6 text-gray mt-2"]/relative-time/@datetime').extract_first()
            item['name'] = course.xpath('.//div[@class="d-inline-block mb-1"]/h3/a/text()').re_first('\n\s*(.*)')
            item['update_time'] = datetime.strptime(time_str,'%Y-%m-%dT%H:%M:%SZ')
            other_item = response.urljoin(course.xpath('.//div[@class="d-inline-block mb-1"]/h3/a/@href').extract_first())
            request = scrapy.Request(other_item, callback = self.parse_other)
            request.meta['item'] = item
            yield request

    def parse_other(self, response):
        item = response.meta['item']
        item['commits'] = response.xpath('//li[@class="commits"]/a/span[@class="num text-emphasized"]/text()').re_first('\s*(.*)\s*')
        item['branches'] = response.xpath('//ul[@class="numbers-summary"]/li[2]/a/span/text()').re_first('\s*(.*)\s*')
        item['releases'] = response.xpath('//ul[@class="numbers-summary"]/li[3]/a/span/text()').re_first('\s*(.*)\s*')
        yield item

    @property
    def start_urls(self):
        url_root = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_root.format(i) for i in range(1,5))

