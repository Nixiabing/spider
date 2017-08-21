@echo off
:s
echo 程序已开始执行，5分钟扫描一次
ping localhost -n 10 > nul
scrapy crawl weibo
scrapy crawl web
  
goto s
pause