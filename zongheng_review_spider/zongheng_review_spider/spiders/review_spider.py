import scrapy
import pandas as pd
from zongheng_review_spider.items import ZonghengReviewSpiderItem
from scrapy import Request


def read_url(location):
    df = pd.read_excel(location)
    forum_list = df[1].tolist()
    bkname_list = df[0].tolist()
    return forum_list,bkname_list

class ReviewSpiderSpider(scrapy.Spider):
    name = 'review_spider'
    allowed_domains = ['forum.zongheng.com']
    # start_urls = ['http://forum.zongheng.com/391797.html']
    # bkname_list = ['good']
    start_urls,bkname_list = read_url(r"/ustc/zongheng_review_spider/forum_list.xlsx")
    # start_urls = start_urls
    # bkname_list = bkname_list

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse,dont_filter=True)

    def parse(self, response):
        item = ZonghengReviewSpiderItem()
        reviews =  response.xpath('//div[@class="for-rp-con"]')
        # print(response.text)
        # print(response.url)
        # print(reviews)
        for review in reviews:
            item['user_name'] = review.xpath('.//div[@class="name"]//text()').extract()
            item['review_content']  = review.xpath('.//div[@class="dec clearfix hide JdecAll "]//text()').extract()
            item['origin_content'] = review.xpath('.//div[@class="for-origin"]//text()').extract()
            item['time'] = review.xpath('.//div[@class="date fl"]//text()').extract()
            item["chapter"] = review.xpath('.//div[@class="for-quote"]/b//text()').extract()
            item['up'] = review.xpath('.//div[@class="fr for-list"]/a[1]//text()').extract()
            item['comment'] = review.xpath('.//div[@class="fr for-list"]/a[2]//text()').extract()
            item['bkname'] = self.bkname_list[self.start_urls.index(response.url)]
            yield item
