# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CityIntroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city_id = scrapy.Field()
    city_name = scrapy.Field()
    country_name = scrapy.Field()
    url = scrapy.Field()
    city_image = scrapy.Field()
    title = scrapy.Field()
    intro = scrapy.Field()
    activity = scrapy.Field()
    pass
