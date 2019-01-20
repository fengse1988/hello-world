# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['sd.sgcc.com.cn']
    start_urls = ['http://www.sd.sgcc.com.cn/html/main/col34/column_34_1.html']
#定义提取url规则
    rules = (
        #linkextractor 链接提取器，提取url地址
        #callback提取url地址交给callback处理
       #follow表示当前url相应是否经过rules来提取--循环。决定是否继续提取url！
        Rule(LinkExtractor(allow=r'/html/main/col8/(\d){4}-(\d){2}/(\d){2}/(\d+)_1.html'), callback='parse_item'),
        #Rule(LinkExtractor(allow=r'/html/main/col8/2019-01/14/(\d+)_1.html'), callback='parse_item'),
    )
#parse函数不能重新定义
    def parse_item(self, response):
        item = {}
        item['title'] = re.findall(r"tag=\"_ddfield\" objid=\"6080\">(.*?)<",response.body.decode())[0]
        content=response.xpath("//div[@objid='6014']//p/text()").extract()
        item['content']=content

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        yield item
