# -*- coding: UTF-8 -*-
import scrapy
import json
import csv
import yagmail
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from tutorial.items import WeiboItem

class WeiboSmtpSpider(scrapy.Spider):
    name = "WeiboSmtp" #scrapy项目名称
    allowed_domains = ["WeiboSmtp.org"]
    start_urls = [
        
    ]# 舆情监测系统的接口，不可外泄！！！
    def parse(self, response):
        js = json.loads(response.body,encoding='utf-8')["result"]
        j = 0
        for s in js:
            i = 0
            if(s["weiboType"] == 2):
                reader = csv.reader(open('weibo.csv'))# 读取已有数据
                for row in reader:
                    weiboId = str(s["weiboId"])# 更改喂字符串格式
                    if (row[2] == weiboId):
                        i = 1
                if(i == 0):
                    data = [
                        s["weiboUrl"],
                        json.dumps(s["weiboUser"],ensure_ascii=False).decode('utf-8').encode('gb18030'),
                        s["weiboId"],
                        s["weiboType"],
                        json.dumps(s["weiboContent"],ensure_ascii=False).decode('utf-8').encode('gb18030')
                    ]#插入csv中的数据
                    writer = csv.writer(open('weibo.csv','ab+'))# 'ab+':在原有的数据基础上进行插入
                    writer.writerow(data)#插入一行数据
                    j = 1
                    # 弹出桌面提示框
                    title = "监测到新的舆情微博!"#标题
                    content = (s["weiboUser"] + ' : ' + s["weiboContent"])#提示内容
                    url = "\n链接：" + s["weiboUrl"]#微博链接
                    yag = yagmail.SMTP(user='', password='', host='smtp.163.com', port='25')
                    yag.send('', title, (content + url))
            '''
            实例化item
            item = WeiboItem()
            item['weiboId'] = s["weiboId"]
            item['weiboUser'] = s["weiboUser"]
            item['weiboHome'] = s["weiboHome"]
            item['weiboContent'] = s["weiboContent"]
            item['weiboType'] = s["weiboType"]
            yield item
            '''
        if(j == 1):
            print("***  INFO:Weibo is updated now!  ***")
        else:
            print("****  INFO:No new weibo~  ***")