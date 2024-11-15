
import scrapy

class DronesSpider(scrapy.Spider):
    name = "drones"
    allowed_domains = ["carbon38.com"]
    start_urls = ["https://carbon38.com/en-in/collections/stillness?filter.p.m.custom.available_or_waitlist=1"]
    def parse(self, response):
        products = response.css('div.ProductItem__Wrapper')
        for product in products:
            item = {
                'title': product.css('h2.ProductItem__Title.Heading a::text').get(),
                'price': product.css('span.ProductItem__Price.Price::text').get(),
                'brand': response.css('h3.ProductItem__Designer::text').get(),
                'colortitle': response.css('label.ColorSwatch::attr(title)').get(),
                'sizes': product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall()



            }
            yield item



# import scrapy
# import csv

# class DronesSpider(scrapy.Spider):
#     name = "drones"
#     allowed_domains = ["carbon38.com"]

#     def __init__(self, start_urls=None, *args, **kwargs):
#         super(DronesSpider, self).__init__(*args, **kwargs)
#         if start_urls:
#             self.start_urls = [start_urls]
#         # Open the CSV file in write mode
#         self.csv_file = open('output.csv', mode='w', newline='', encoding='utf-8')
#         self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=['title', 'price', 'brand', 'colortitle', 'sizes'])
#         self.csv_writer.writeheader()  # Write the header to the CSV file

#     def parse(self, response):
#         # Extract product details
#         products = response.css('div.ProductItem__Wrapper')
#         for product in products:
#             item = {
#                 'title': product.css('h2.ProductItem__Title.Heading a::text').get(),
#                 'price': product.css('span.ProductItem__Price.Price::text').get(),
#                 'brand': product.css('h3.ProductItem__Designer::text').get(),
#                 'colortitle': product.css('label.ColorSwatch::attr(title)').get(),
#                 'sizes': product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall()
#             }
#             # Write the item to the CSV file
#             self.csv_writer.writerow(item)
#             yield item

#     def close(self, reason):
#         # Close the CSV file after finishing the scraping
#         self.csv_file.close()


# import scrapy

# class DronesSpider(scrapy.Spider):
#     name = "drones"
#     allowed_domains = ["carbon38.com"]

#     # Use start_requests to read URLs from an external file
#     def start_requests(self):
#         # Open the file and read each line as a URL
#         with open('links.txt', 'r') as f:
#             urls = f.read().splitlines()
#             for url in urls:
#                 # Send each URL to the parse function
#                 yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         # Select all products on the page
#         products = response.css('div.ProductItem__Wrapper')
#         for product in products:
#             # Extract product details from each product
#             item = {
#                 'title': product.css('h2.ProductItem__Title.Heading a::text').get(),
#                 'price': product.css('span.ProductItem__Price.Price::text').get(),
#                 'brand': product.css('h3.ProductItem__Designer::text').get(),
#                 'colortitle': product.css('label.ColorSwatch::attr(title)').get(),
#                 'sizes': product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall()
#             }
#             yield item

# import scrapy

# class DronesSpider(scrapy.Spider):
#     name = "drones"
#     allowed_domains = ["carbon38.com"]

#     def __init__(self, start_urls=None, *args, **kwargs):
#         super(DronesSpider, self).__init__(*args, **kwargs)
#         # Set the start_urls dynamically from the passed argument
#         if start_urls:
#             self.start_urls = [start_urls]

#     def parse(self, response):
#         # Extract the product details
#         products = response.css('div.ProductItem__Wrapper')
#         for product in products:
#             item = {
#                 'title': product.css('h2.ProductItem__Title.Heading a::text').get(),
#                 'price': product.css('span.ProductItem__Price.Price::text').get(),
#                 'brand': product.css('h3.ProductItem__Designer::text').get(),
#                 'colortitle': product.css('label.ColorSwatch::attr(title)').get(),
#                 'sizes': product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall()
#             }
#             yield item


# import scrapy

# class DronesSpider(scrapy.Spider):
#     name = "drones"
#     allowed_domains = ["carbon38.com"]

#     # Specify the path to the file containing the links
#     links_file = 'links.txt'

#     def start_requests(self):
#         # Open the file and read each line as a URL
#         with open(self.links_file, 'r') as f:
#             urls = f.read().splitlines()
#             for url in urls:
#                 # Create a request for each URL, passing it to `parse_product`
#                 yield scrapy.Request(url=url, callback=self.parse_product)

#     def parse_product(self, response):
#         # Extract the required fields from each product detail page
#         item = {
#             'title': response.css('h1.ProductMeta__Title::text').get().strip(),
#             'price': response.css('span.ProductMeta__Price.Price::text').get(),
#             'brand': response.css('h3.ProductItem__Designer::text').get(),
#             'colortitle': response.css('label.ColorSwatch::attr(title)').get()
#         }
#         yield item




# import scrapy

# class DronesSpider(scrapy.Spider):
#     name = "drones"
#     allowed_domains = ["carbon38.com"]
#     start_urls = ["https://carbon38.com/en-in/collections/shoes?filter.p.m.custom.available_or_waitlist=1"]

#     def parse(self, response):
#         # Extract and follow each product link
#         product_links = response.css('div.ProductItem__Wrapper a::attr(href)').getall()
#         for link in product_links:
#             yield response.follow(link, callback=self.parse_product)

#     def parse_product(self, response):
#         # Extract the required fields from each product detail page
#         item = {
#             'title': response.css('h1.ProductMeta__Title::text').get().strip(),
#             'price': response.css('span.ProductMeta__Price.Price::text').get(),
#             'brand': response.css('h3.ProductItem__Designer::text').get(),
#             'colortitle': response.css('label.ColorSwatch::attr(title)').get(),
#             'sizes': [size.strip() for size in response.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall() if size.strip()]
#         }
#         yield item

