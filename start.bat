@echo off
:s
echo �����ѿ�ʼִ�У�5����ɨ��һ��
ping localhost -n 10 > nul
scrapy crawl weibo
scrapy crawl web
  
goto s
pause