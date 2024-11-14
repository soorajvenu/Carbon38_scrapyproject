import scrapy

class ShoesSpider(scrapy.Spider):
    name = 'shoes'
    allowed_domains = ['carbon38.com']
    start_urls = ['https://carbon38.com/en-in/collections/shoes?filter.p.m.custom.available_or_waitlist=1']

    def parse(self, response):
        # Selecting the product list section (Modify the CSS selector according to the site structure)
        products = response.css('div.product-grid__item')  # Update CSS selector as per HTML structure

        for product in products:
            yield {
                'name': product.css('h2.product-card__title::text').get(),
                'price': product.css('span.price__sale::text').get(),
                'availability': product.css('div.product-card__availability::text').get(),
                'link': response.urljoin(product.css('a::attr(href)').get())
            }

        # Pagination - Check if there is a next page
        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
