import scrapy
from fpt_phone.items import FptPhoneItem

class DataphoneSpider(scrapy.Spider):
    name = 'dataphone'
    allowed_domains = ['cellphones.com.vn']
    # start_urls = ['https://cellphones.com.vn/mobile/apple/iphone-13.html']
    # start_urls = ['https://cellphones.com.vn/mobile/samsung.html']
    # start_urls = ['https://cellphones.com.vn/mobile/xiaomi.html']
    # start_urls = ['https://cellphones.com.vn/mobile/oppo.html']
    # start_urls = ['https://cellphones.com.vn/mobile/nokia.html']
    # start_urls = ['https://cellphones.com.vn/mobile/realme.html']
    # start_urls = ['https://cellphones.com.vn/mobile/vsmart.html']
    start_urls = ['https://cellphones.com.vn/mobile/vivo.html']


    def parse(self, response):
       product=response.css('.item-product')
       for p in product:
                name = p.css('div.item-product__box-name > a > h3::text').extract_first()
                memory_storage= p.css('div.item-product__more-info > p::text').getall()
                price = p.css('.old-price::text').extract_first()
                price_selloff = p.css('.special-price::text').extract_first()
                ratings =  p.css('div.item-product__box-raiting::text').extract()
                # print(name,memory_storage,price,price_selloff,ratings)
                item=FptPhoneItem()
                item['name']= name
                item['memory_storage']=memory_storage
                item['price'] = price
                item['price_selloff']=price_selloff
                item['ratings'] = ratings
                yield item