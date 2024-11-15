import subprocess

# Read URLs from links.txt
with open('/home/dell/scrapyproject/Carbon38_scrapyproject/my_scrapy_project/my_scrapy_project/spiders/links.txt', 'r') as file:
    urls = file.read().splitlines()

# Run the spider for each URL
for url in urls:
    # Pass the URL to the spider as a custom setting for start_urls
    subprocess.run(['scrapy', 'crawl', 'drones', '-a', f'start_urls={url}'])
