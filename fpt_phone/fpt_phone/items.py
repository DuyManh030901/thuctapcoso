# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FptPhoneItem(scrapy.Item):
    name = scrapy.Field()
    memory_storage = scrapy.Field()
    price = scrapy.Field()
    price_selloff = scrapy.Field()
    ratings = scrapy.Field()

    
#    name = p.css('div.item-product__box-name > a > h3::text').extract_first()
#                 memory_storage= p.css('div.item-product__more-info >  p::text').getall()[-1]
#                 price = p.css('.old-price::text').extract_first()
#                 price_selloff = p.css('.special-price::text').extract_first()
#                 ratings =  p.css('div.item-product__box-raiting::text').extract()
#                 print(name,memory_storage,price,price_selloff,ratings)
