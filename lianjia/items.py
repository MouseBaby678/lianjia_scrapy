# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    totalprice = scrapy.Field()
    unitprice = scrapy.Field()
    community = scrapy.Field()
    position = scrapy.Field()
    fangwuhuxing = scrapy.Field()
    louceng = scrapy.Field()
    jianzhumianji = scrapy.Field()
    huxingjiegou = scrapy.Field()
    taoneimianji = scrapy.Field()
    jianzhuleixing = scrapy.Field()
    fangwuchaoxiang = scrapy.Field()
    jianzhujiegou = scrapy.Field()
    zhuangxiuqingkuang = scrapy.Field()
    tihubili = scrapy.Field()
    gongnuanfangshi = scrapy.Field()
    peibeidianti = scrapy.Field()
    guapaishijian = scrapy.Field()
    pass
