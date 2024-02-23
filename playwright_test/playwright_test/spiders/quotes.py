# spiders/quotes.py

import scrapy
from playwright_test.items import QuoteItem
from scrapy_playwright.page import PageMethod

class QuotesSpider(scrapy.Spider):
	name = 'quotes'

	def start_requests(self):
		url = "https://quotes.toscrape.com/js/"
		yield scrapy.Request(url, meta=dict(
				playwright = True,
				playwright_include_page = True, 
				playwright_page_methods =[
          PageMethod("wait_for_selector", "div.quote"),
          ]
			))

	async def parse(self, response):
		page = response.meta["playwright_page"]
		screenshot = await page.screenshot(path="example.png", full_page=True)
          # screenshot contains the image's bytes
		await page.close()
  