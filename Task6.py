#Use the Scrapy Libray
import scrapy
#Create a class for scrapy
class NewSpider(scrapy.Spider):
    name = 'new_spider'
    start_urls = ['http://172.17.50.43/freebix']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image link': x.xpath(newsel).extract_first(),
            }