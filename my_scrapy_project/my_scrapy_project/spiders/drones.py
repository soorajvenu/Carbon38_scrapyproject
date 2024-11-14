import scrapy

class DronesSpider(scrapy.Spider):
    name = "drones"
    allowed_domains = ["carbon38.com"]
    start_urls = ["https://carbon38.com/en-in/collections/tops?filter.p.m.custom.available_or_waitlist=1"]

    def parse(self, response):
        products = response.css('div.ProductItem__Wrapper')
        for product in products:
            item = {
                'title': product.css('h2.ProductItem__Title.Heading a::text').get(),
                'price': product.css('span.ProductItem__Price.Price::text').get()
            }
            yield item
