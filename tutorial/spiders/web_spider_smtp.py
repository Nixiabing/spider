# -*- coding: UTF-8 -*-
import scrapy
import json
import csv
import yagmail
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from tutorial.items import WebItem

class WebSmtpSpider(scrapy.Spider):
    name = "WebSmtp" #scrapy项目名称
    allowed_domains = ["WebSmtp.org"]
    start_urls = [
        
    ]# 舆情监测系统的接口，不可外泄！！！
    def parse(self, response):
        js = json.loads(response.body,encoding='utf-8')["result"]
        j = 0
        for s in js:
            i = 0
            if(s["webType"] == 2):
                reader = csv.reader(open('web.csv'))# 读取已有数据
                for row in reader:
                    weiboId = str(s["webId"])# 更改喂字符串格式
                    if (row[2] == weiboId):
                        i = 1
                if(i == 0):
                    data = [
                        json.dumps(s["webTitle"],ensure_ascii=False).decode('utf-8').encode('gb18030'),
                        s["webUrl"],
                        s["webId"],
                        json.dumps(s["webSource"],ensure_ascii=False).decode('utf-8').encode('gb18030'),
                        s["webType"],
                        json.dumps(s["webDes"],ensure_ascii=False).decode('utf-8').encode('gb18030')
                    ]#插入csv中的数据
                    writer = csv.writer(open('web.csv','ab+'))# 'ab+':在原有的数据基础上进行插入
                    writer.writerow(data)#插入一行数据
                    j = 1
                    # 弹出桌面提示框
                    title = "监测到新的舆情报道!"#标题
                    content = (s["webSource"] + ' : ' + s["webTitle"])#提示内容
                    url = "\n链接：" + s["webUrl"]#微博链接
                    yag = yagmail.SMTP(user='', password='', host='smtp.163.com', port='25')
                    yag.send('', title.decode('utf8').encode('gbk'), (content + url))
        if(j == 1):
            print("***  INFO:Web is updated now!  ***")
        else:
            print("****  INFO:No new web~  ***")
        '''
        实例化item
                item = WebItem()
                item['webId'] = s["webId"]
                item['webSource'] = s["webSource"]
                item['webTitle'] = s["webTitle"]
                item['webDes'] = s["webDes"]
                item['webUrl'] = s["webUrl"]
                item['webType'] = s["webType"]
                yield item
        '''