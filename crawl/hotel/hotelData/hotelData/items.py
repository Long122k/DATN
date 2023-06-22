# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelDataItem(scrapy.Item):
    # hotel_url = scrapy.Field()
    hotel_name = scrapy.Field()
    total_hotel_reviews = scrapy.Field()
    star = scrapy.Field()
    hotel_address = scrapy.Field()
    price = scrapy.Field()
    review_date = scrapy.Field()
    reviewer_rating = scrapy.Field()
    reviewer_contribution = scrapy.Field()
    reviewer_link = scrapy.Field()
    reviewer_title_comment = scrapy.Field()
    reviewer_comment = scrapy.Field()
    reviewer_stay_date = scrapy.Field()
    reviewer_trip_type = scrapy.Field()


    # pass
    pass
