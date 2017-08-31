# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WeiboItem(scrapy.Item):
    weiboId = scrapy.Field()#微博ID（唯一）
    weiboUser = scrapy.Field()#微博用户名
    weiboHome = scrapy.Field()#微博地址
    weiboContent = scrapy.Field()#微博内容
    weiboType = scrapy.Field()#检测重要性（0：轻微；2：严重）

class WebItem(scrapy.Item):
    webId = scrapy.Field()#报道ID（唯一）
    webSource = scrapy.Field()#报道媒体
    webTitle = scrapy.Field()#报道标题
    webDes = scrapy.Field()#主要内容
    webUrl = scrapy.Field()#报道网址
    webType = scrapy.Field()#检测重要性（0：轻微；2：严重）

class VideoItem(scrapy.Item):
    videoId = scrapy.Field()#视频ID（唯一）
    sourceName = scrapy.Field()#视频媒体
    videoTitle = scrapy.Field()#视频标题
    videoUrl = scrapy.Field()#报道网址