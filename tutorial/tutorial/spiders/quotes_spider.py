'''
https://doc.scrapy.org/en/latest/intro/tutorial.html
'''

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes" #Name of spider. Must be unique within a project

    
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]
     

    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first(),
    #             'tags': quote.css('div.tags a.tag::text').extract(),
    #         }


    def start_requests(self):
            urls = [
                'http://studentssp.wit.ie/Timetables/POSTT.aspx',
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        