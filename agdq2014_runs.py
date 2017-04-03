import scrapy
import datetime
import re

# Donation page spider
class DonationSpider(scrapy.Spider):
        name = 'donations'

        def start_requests(self):
                url = 'https://gamesdonequick.com/tracker/runs/agdq2014'
                yield scrapy.Request(url=url, callback=self.parse)

        def parse(self, response):
                for row in response.xpath('//table/tr'):
                        #print(row.css('td').extract())
                        yield {
                                'game': row.css('a::text').extract_first(),
                                'players': clean_html(row.css('td').extract()[1]),
                                'description': clean_html(row.css('td').extract()[2]),
                                'starttime': row.css('.datetime::text').extract()[0],
                                'endtime': row.css('.datetime::text').extract()[1],
                                'bidwars': clean_html(row.css('td').extract()[5])
                        }

def clean_html(raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext.strip()