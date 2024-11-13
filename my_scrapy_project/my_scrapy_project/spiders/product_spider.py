import scrapy
from scrapy_splash import SplashRequest

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    start_urls = [
        "https://www.carbon38.com/product/tessa-top-primary-stripe"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        yield {
            # Product name using the updated selector for `.ProductMeta__Title`
            "product_name": response.css(".ProductMeta__Title::text").get(),
            # Add other fields as needed
        }
