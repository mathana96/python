'''
https://blog.scrapinghub.com/2016/04/20/scrapy-tips-from-the-pros-april-2016-edition/
'''

import scrapy
from scrapy.selector import Selector

class SpidyQuotesViewStateSpider(scrapy.Spider):
	name = "spidyquotes"
	start_urls = ['http://studentssp.wit.ie/Timetables/RoomTT.aspx']
	download_delay = 1.5

	# def parse(self, response):
	#     room = response.css('select#CboLocation > option ::attr(value)').extract_first()
		# starttime = '6'
		# endtime = '7'
	#     weeks = '28'
	#     school = '%'
	#     dept = '%'

	#     yield scrapy.FormRequest(
	#         'http://studentssp.wit.ie/Timetables/RoomTT.aspx',
	#         formdata={
	#             'cboSchool': school,
	#             'CboWeeks': weeks,
	#             'CboDept': dept,
	#             'CboStartTime': starttime,
	#             'CboEndTime': endtime,
	#             'CboLocation': room,
	#             '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
	#         },
	#         callback=self.parse_r
	#     )

	def parse(self, response):
		starttime = '6'
		endtime = '7'
		for room in response.css('select#CboLocation > option ::attr(value)').extract():
			yield scrapy.FormRequest.from_response(
				response,
				formdata={'CboLocation': room},
				callback=self.parse_results,
			)

	def parse_r(self, response):
		page = response.url.split("/")[-2]
		filename = 'quotes-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)

	def parse_results(self, response):
		# table = response.xpath('td::attr(align)').extract
		# table = response.css("div#divTT > table > tbody > tr ::text")
		# sel.xpath('//table[@class="bgWhite listTable"]//h3')
		# for quote in response.css("div#divTT"):
		# items = hxs.select('//table[@class="tableh/td')
		hxs = Selector(response)
		rows = hxs.xpath('//tr')
		for row in rows:
			print row.select('td/text()').extract()
		# yield {
		# 	'room': table,
		# }