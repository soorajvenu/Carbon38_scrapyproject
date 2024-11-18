
# import scrapy

# class DronesSpider(scrapy.Spider):
#     name = "drones"
#     allowed_domains = ["carbon38.com"]
#     start_urls = ["https://carbon38.com/en-in/collections/stillness?filter.p.m.custom.available_or_waitlist=1"]
#     def parse(self, response):
#         products = response.css('div.ProductItem__Wrapper')
#         for product in products:
#             item = {
#                 'title': product.css('h2.ProductItem__Title.Heading a::text').get(),
#                 'price': product.css('span.ProductItem__Price.Price::text').get(),
#                 'brand': response.css('h3.ProductItem__Designer::text').get(),
#                 'colortitle': response.css('label.ColorSwatch::attr(title)').get(),
#                 'sizes': product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall()



#             }
#             yield item
# import scrapy
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from scrapy.selector import Selector
# import time

# class DronesSpider(scrapy.Spider):
#     name = "drones"
#     allowed_domains = ["carbon38.com"]
#     start_urls = ["https://carbon38.com/en-in/collections/clothing?filter.p.m.custom.available_or_waitlist=1&filter.p.m.custom.available_or_waitlist=1&page=1&filter.p.m.custom.available_or_waitlist=1"]

#     def __init__(self, *args, **kwargs):
#         super(DronesSpider, self).__init__(*args, **kwargs)
        
#         # Provide the path to ChromeDriver directly
#         chrome_driver_path = "/home/dell/scrapyproject/Carbon38_scrapyproject/my_scrapy_project/my_scrapy_project/chromedriver"  # Replace with the actual path to your downloaded ChromeDriver
#         self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
#         self.driver.implicitly_wait(10)

#     def parse(self, response):
#         # Open the URL with Selenium
#         self.driver.get(self.start_urls[0])

#         while True:
#             # Create a Scrapy Selector from the Selenium page source
#             sel = Selector(text=self.driver.page_source)

#             # Extract product information
#             products = sel.css('div.ProductItem__Wrapper')
#             for product in products:
#                 item = {
#                     'title': product.css('h2.ProductItem__Title.Heading a::text').get(),
#                     'price': product.css('span.ProductItem__Price.Price::text').get(),
#                     'brand': product.css('h3.ProductItem__Designer::text').get(),
#                     'colortitle': product.css('label.ColorSwatch::attr(title)').get(),
#                     'sizes': product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall(),
#                 }
#                 yield item

#             # Find the next page URL from the href attribute
#             next_page = sel.css('div.Pagination__Nav a.Pagination__NavItem.Link.Link--primary::attr(href)').get()
#             if next_page:
#                 next_page_url = response.urljoin(next_page)
#                 self.driver.get(next_page_url)
#                 time.sleep(3)  # Wait for the page to load
#             else:
#                 break  # Exit loop if there is no next page

#         # Close the Selenium driver after finishing the pagination
#         self.driver.quit()

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from scrapy.selector import Selector
import time

class DronesSpider(scrapy.Spider):
    name = "drones"
    allowed_domains = ["carbon38.com"]
    start_urls = ["https://carbon38.com/en-in/collections/clothing?filter.p.m.custom.available_or_waitlist=1"]

    def __init__(self, *args, **kwargs):
        super(DronesSpider, self).__init__(*args, **kwargs)
        
        # Provide the path to ChromeDriver directly
        chrome_driver_path = "/home/dell/scrapyproject/Carbon38_scrapyproject/my_scrapy_project/my_scrapy_project/chromedriver"  # Replace with the actual path to your downloaded ChromeDriver
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
        self.driver.implicitly_wait(10)

    def parse(self, response):
        # Open the URL with Selenium
        self.driver.get(self.start_urls[0])

        while True:
            # Create a Scrapy Selector from the Selenium page source
            sel = Selector(text=self.driver.page_source)

            # Extract product information
            products = sel.css('div.ProductItem__Wrapper')
            for product in products:
                item = {
                    'title': product.css('h2.ProductItem__Title.Heading a::text').get(),
                    'price': product.css('span.ProductItem__Price.Price::text').get(),
                    'brand': product.css('h3.ProductItem__Designer::text').get(),
                    'colortitle': product.css('label.ColorSwatch::attr(title)').get(),
                    'sizes': product.css('div.ProductItem__SizeVariants a.add-size-to-cart::text').getall(),
                    'imageurl': product.css('img.ProductItem__Image::attr(src)').get(),
                    'reviews': product.css('div.yotpo-sr-bottom-line-text.yotpo-sr-bottom-line-text--right-panel::text').get(),
                }
                yield item

            # Find the next page URL from the href attribute
            next_page = sel.css('div.Pagination__Nav a.Pagination__NavItem.Link.Link--primary::attr(href)').get()
            if next_page:
                next_page_url = response.urljoin(next_page)
                self.driver.get(next_page_url)
                time.sleep(3)  # Wait for the page to load
            else:
                break  # Exit loop if there is no next page

        # Close the Selenium driver after finishing the pagination
        self.driver.quit()



