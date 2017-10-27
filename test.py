"""import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
"""

import bee

if __name__ == "__main__":
  bee.site.lu.p2p.open_transfer_p2p_invest_page()

  from selenium import webdriver

  browser = webdriver.Chrome("/Users/polly/Downloads/chromedriver", port=9515)
  page = browser.get("http:/www.baidu.com/")
