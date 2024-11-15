import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    allowed_domains = ["carbon38.com"]
    start_urls = [
        "https://carbon38.com/en-in/collections/tops?filter.p.m.custom.available_or_waitlist=1"
    ]

    def parse(self, response):
        # Loop through all product links on the page
        product_links = response.css('a.ProductItem__ImageWrapper::attr(href)').getall()
        for link in product_links:
            # Follow each link to the product's detail page
            yield response.follow(link, self.parse_product)

    def parse_product(self, response):
        # Extract detailed product information
        item = {
            "breadcrumbs": response.css('nav.Breadcrumbs a::text').getall(),
            "primary_image_url": response.css('img.Product__SlideItem--image::attr(src)').get(),
            "brand": response.css('span.ProductMeta__Brand::text').get().strip(),
            "product_name": response.css('h1.ProductMeta__Title::text').get().strip(),
            "price": response.css('span.ProductMeta__Price.Price::text').get(),
            "reviews": response.css('span.ProductReviewStars__Count::text').get() or "0 Reviews",
            "colour": response.css('span.ProductForm__OptionName::text').get(),
            "sizes": response.css('select.ProductForm__SizeOption option::text').getall(),
            "description": response.css('div.ProductMeta__Description p::text').get(),
            "sku": response.css('span.ProductMeta__SKU::text').get(),
            "product_id": response.css('div[data-product-id]::attr(data-product-id)').get(),
            "product_url": response.url,
            "image_urls": response.css('img.Product__SlideItem--image::attr(src)').getall(),
        }
        yield item
