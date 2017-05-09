import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from douban_reading.items import DoubanBookItem

class BookSpider(scrapy.Spider):
    """docstring for BookSpider"""
    name = 'douban_reading_test'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        # url = 'https://book.douban.com/subject/6082808/'
        url = 'https://book.douban.com/subject/1008145/'
        yield Request(url, headers=self.headers, callback = self.parseInfo)

    def parseInfo(self, response):

        item = DoubanBookItem()
        book_info = response.xpath('//div[@id="info"]/span')
        item['title'] = response.xpath('//h1/span[1]/text()').extract()[0]
        item['info_array'] = []
        # basic book info
        for info_item in book_info:
            item['info_array'].append(info_item.xpath('.//following-sibling::text()').extract()[0])

        # book authors
        item['authors'] = []
        authors = response.xpath('//div[@id="info"]/a')
        for author in authors:
            item['authors'].append(author.xpath('.//text()').extract()[0])

        # rating people
        rating = response.xpath('//div[@id="interest_sectl"]')
        item['rating_people'] = rating.xpath('.//a[@class="rating_people"]/span/text()').extract()[0]
        item['rates'] = rating.xpath('.//strong[@class="ll rating_num "]/text()').extract()[0]

        commits = response.xpath('//h2')
        item['commits_short'] = commits.xpath('./span/a/text()').re(r'(\d+)')[0]

        item['commits_long'] = commits.xpath('./span/a/text()').re(r'(\d+)')[1]

        item['notes_number'] = response.xpath('//h2/span/a/span/text()').extract()[0]
        item['read'] = response.xpath('//div[@id="collector"]/p/a/text()').re(r'(\d+)人读过')[0]
        item['reading'] = response.xpath('//div[@id="collector"]/p/a/text()').re(r'(\d+)人在读')[0]
        item['want_read'] = response.xpath('//div[@id="collector"]/p/a/text()').re(r'(\d+)人想读')[0]

        yield item

    def genUrls(self, start_url):
        pass
