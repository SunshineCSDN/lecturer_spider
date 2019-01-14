爬取网站讲师的姓名、职称和个人信息。
参考网址()https://segmentfault.com/a/1190000013178839
scrapy.cfg ：项目的配置文件

testscrapy/ ：项目的Python模块，将会从这里引用代码

testscrapy/items.py ：项目的目标文件

testscrapy/pipelines.py ：项目的管道文件

testscrapy/settings.py ：项目的设置文件

testscrapy/spiders/ ：存储爬虫代码目录



scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件
1.json格式，默认为Unicode编码
scrapy crawl itcast -o teachers.json
2.json lines格式，默认为Unicode编码
scrapy crawl itcast -o teachers.jsonl
3.csv 逗号表达式，可用Excel打开
scrapy crawl itcast -o teachers.csv
4.xml格式
scrapy crawl itcast -o teachers.xml