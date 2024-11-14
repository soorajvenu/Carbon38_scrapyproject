import scrapy


class Product_spiderSpider(scrapy.Spider):
    name = 'Product_spider'
    allowed_domains = ['carbon38.com/en-in/collections/tops']
    start_urls = ['https://carbon38.com/en-in/collections/tops']

    def parse(self, response):
        products = response.css('div.ProductItem__Warapper')
        for product in products:
            item = {
            'title' : product.css('h2.ProductItem__Title.Heading a::text').getall(),
            'price' : product.css('span.ProductItem__Price.Price::text').getall()
            }
            yield item 
        pass