@echo off
:s
echo �����ѿ�ʼִ�У�5����ɨ��һ��
ping localhost -n 300 > nul
scrapy crawl weibo
scrapy crawl web
  
goto s
pause