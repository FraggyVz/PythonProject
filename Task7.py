import scrapy
#Use the previous task script
class NewSpider(scrapy.Spider):
    name = 'new_spider'
    start_urls = ['http://172.17.50.43/freebix']
    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image link': x.xpath(newsel).extract_first(),
            }
#To recurse new page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )