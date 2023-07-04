# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelItem(scrapy.Item):
    hotel_url = scrapy.Field()
    hotel_id = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
    # city_id = scrapy.Field()
    pass
