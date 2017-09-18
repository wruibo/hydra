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

import threading

class T(threading.Thread):
    def start(self):
        threading.Thread.start(self)

    def stop(self):
        self.join()

    def run(self):
        print("hello")

if __name__ == "__main__":
    #s = QuotesSpider()
    #for a in s.start_requests():
    #    b = s.handles_request(a)
    #    s.parse(b)
    t = T()
    t.start()
    t.stop()