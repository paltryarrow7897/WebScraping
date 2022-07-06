import scrapy

class RecipeSpider(scrapy.Spider):
 name = "recipe_spider"
 start_urls = ["https://www.yummly.com/recipes"]

 def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)