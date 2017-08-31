# -*- coding: UTF-8 -*-
import scrapy
import json
import csv
import win32api
import winsound
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from tutorial.items import VideoItem

class VideoSpider(scrapy.Spider):
    name = "video" #scrapy项目名称
    allowed_domains = ["video.org"]
    start_urls = [
        ""
    ]# 舆情监测系统的接口，不可外泄！！！
    def parse(self, response):
        js = json.loads(response.body,encoding='utf-8')["result"]
        j = 0
        for s in js:
            i = 0
            reader = csv.reader(open('video.csv'))# 读取已有数据
            for row in reader:
                videoId = str(s["videoId"])# 更改喂字符串格式
                if (row[3] == videoId):
                    i = 1
            if(i == 0):
                data = [
                    json.dumps(s["sourceName"],ensure_ascii=False).decode('utf-8').encode('gb18030'),
                    json.dumps(s["videoTitle"],ensure_ascii=False).decode('utf-8').encode('gb18030'),
                    s["videoUrl"],
                    s["videoId"],
                ]#插入csv中的数据
                writer = csv.writer(open('video.csv','ab+'))# 'ab+':在原有的数据基础上进行插入
                writer.writerow(data)#插入一行数据
                j = 1
                wav = 'sound.wav'#音频名称
                winsound.PlaySound(wav, winsound.SND_NODEFAULT)#播发提示音
                # 弹出桌面提示框
                title = "监测到新的新闻视频!"#标题
                content = (s["sourceName"] + ' : ' + s["videoTitle"])#提示内容
                url = "\n链接：" + s["videoUrl"]#微博链接
                win32api.MessageBox(0, (content + url).decode('utf8').encode('gbk'), title.decode('utf8').encode('gbk'))
        if(j == 1):
            print("***  INFO:Video is updated now!  ***")
        else:
            print("****  INFO:No new Video~  ***")
        '''
        #实例化item
        item = VideoItem()
        item['videoId'] = s["videoId"]
        item['sourceName'] = s["sourceName"]
        item['videoTitle'] = s["videoTitle"]
        item['videoUrl'] = s["videoUrl"]
        yield item
        '''