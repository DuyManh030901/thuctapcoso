import scrapy

class DataphoneSpider(scrapy.Spider):
    name = 'dataphone'
    allowed_domains = ['www.nguyenkim.com']
    start_urls = ['https://www.nguyenkim.com/dien-thoai-di-dong-samsung/']

    def parse(self, response):
        response.css()
        product=response.css('.item').extract()
