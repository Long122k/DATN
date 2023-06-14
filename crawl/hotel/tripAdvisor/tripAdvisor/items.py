# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class TripadvisorItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     hotel_url = scrapy.Field()
#     hotel_name = scrapy.Field()
#     total_hotel_reviews = scrapy.Field()
#     hotel_address = scrapy.Field()
#     reviewer_rating = scrapy.Field()
#     reviewer_contribution = scrapy.Field()
#     reviewer_helpful_vote = scrapy.Field()
#     reviewer_title_comment = scrapy.Field()
#     reviewer_comment = scrapy.Field()
#     reviewer_stay_date = scrapy.Field()
#     reviewer_trip_type = scrapy.Field()


    # pass

class HotelItem(scrapy.Item):
    hotel_url = scrapy.Field()
    hotel_id = scrapy.Field()
    # city_id = scrapy.Field()
    pass
