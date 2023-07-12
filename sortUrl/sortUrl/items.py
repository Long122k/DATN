# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SorturlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    reviews = scrapy.Field()
    city = scrapy.Field()
    country = scrapy.Field()
    hotel_id = scrapy.Field()
    pass
