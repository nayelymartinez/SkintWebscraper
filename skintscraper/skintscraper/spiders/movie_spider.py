import scrapy

class MovieSpider(scrapy.Spider):
	name = 'movies'

	def start_requests(self):
		urls = [
			'http://theskint.com'
		]
		for url in urls:
			yield scrapy.Request(url = url, callback = self.parse)

	def parse(self, response):
		with open('movies', 'wb') as f:
			f.write(response.body)
		self.log('saved file.')

	def retrieve_movies(self):
		f = open('movies.txt', 'r')
		print(f)