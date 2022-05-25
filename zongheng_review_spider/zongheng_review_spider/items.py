# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ZonghengReviewSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # user_info_url = scrapy.Field()
    user_name = scrapy.Field()
    review_content = scrapy.Field()
    origin_content = scrapy.Field()
    chapter = scrapy.Field()
    time = scrapy.Field()
    up = scrapy.Field()
    comment = scrapy.Field()
    bkname = scrapy.Field()
