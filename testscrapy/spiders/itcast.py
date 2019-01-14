# -*- coding: utf-8 -*-
import scrapy
from testscrapy.items import TestscrapyItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)

    def parse(self, response):
#         filename = "teachers.html"
#         open(filename, 'w',encoding='utf-8'
# ).write(response.body.decode())

    # 存放老师信息的集合
        items = []

        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = TestscrapyItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            level = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['level'] = level[0]
            item['info'] = info[0]

            items.append(item)

        # 直接返回最后数据
        return items