import scrapy
import datetime

# Donation page spider
class DonationSpider(scrapy.Spider):
        name = 'donations'

        def start_requests(self):
                urls = []
                for x in range(1, 46):
                        urls.append('https://gamesdonequick.com/tracker/donations/sgdq2012?page=' + str(x))
                for url in urls:
                        yield scrapy.Request(url=url, callback=self.parse)

        def parse(self, response):
                for row in response.xpath('//table/tr'):
                        if '(Anonymous)' not in row.css('td::text').extract_first():
                                yield {
                                        'donorURI': row.css('a::attr(href)').extract_first(),
                                        'time': row.css('.datetime::text').extract_first(),
                                        'amount': row.css('td a::text').extract()[1][1:],
                                        'comment': row.css('td::text').extract()[6].replace('\n', '')
                                }
                        else:
                                yield {
                                        'donorURI': '',
                                        'time': row.css('.datetime::text').extract_first(),
                                        'amount': row.css('td a::text').extract()[0][1:],
                                        'comment': row.css('td::text').extract()[5].replace('\n', '')
                                }
