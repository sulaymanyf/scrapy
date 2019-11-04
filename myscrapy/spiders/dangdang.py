# -*- coding: utf-8 -*-
import scrapy


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/childrensbooks/01.41.00.00.00.00-24hours-0-0-1-1-bestsell']

    def parse(self, response):
        book_list = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]')
        print("开始")
        for book in book_list:
            print(len(book_list))
            item = {}
            #
            item['book_name'] = book.xpath('//div[@class="name"]/a/text()').extract_first()
            item['book_publisher'] = book.xpath('//div[@class="publisher_info"]/a//text()').extract()[0:3]
            item['book_price'] = book.xpath('//div[@class="price_r"]/span[@class="price_r"]/text()').extract_first()
            print(item)
