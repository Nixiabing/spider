@echo off
:s
echo �����ѿ�ʼִ�У�5����ɨ��һ��
ping localhost -n 300 > nul
scrapy crawl WeiboSMTP
scrapy crawl WebSMTP
scrapy crawl VideoSMTP
  
goto s
pause