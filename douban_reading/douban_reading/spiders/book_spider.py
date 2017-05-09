import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from douban_reading.items import DoubanBookItem

class BookSpider(scrapy.Spider):
    """docstring for BookSpider"""
    name = 'douban_reading'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://book.douban.com/subject/6082808/'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanBookItem()
        book_info = response.xpath('//div[@id="info"]/br')
        # read = response.xpath('//')
        item['title'] = response.xpath('//h1/span[1]/text()').extract()[0]
        # item['tag'] = book_info.xpath('.//')
        # item['read'] = book_info.xpath('.//.')
        item['info_array'] = []
        # i = 0
        for info_item in book_info:
            item['info_array'].append(info_item.xpath('.//preceding-sibling::text()').extract()[0])
            # i += 1
        # item['publication'] = 
        yield item