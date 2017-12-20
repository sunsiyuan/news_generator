# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from toutiao_bot.items import News
import json
import logging

class toutiao_spider(Spider):
    name = "toutiao"
    allowed_domains = ["www.toutiao.com"]
    start_urls = ['https://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A1B50A73143B807&cp=5A344BD8C097CE1&_signature=W1mexQAAAW2DXMbfgi-38FtZnt']
    url='https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time={behot_time}&max_behot_time_tmp={behot_time_tmp}&tadrequire=true&as=A1B50A73143B807&cp=5A344BD8C097CE1&_signature=W1mexQAAAW2DXMbfgi-38FtZnt'
    
    def parse(self, response):
        jsonData=json.loads(response.body.decode("utf-8"))
        MainData=jsonData["data"]
        nextTime=jsonData["next"]["max_behot_time"]
        if jsonData["message"]=='success':
            for rowData in MainData:
                item = News()
                item['title'] = rowData.get('title')
                item['tag'] = rowData.get('tag')
                item['label'] = rowData.get('label')
                item['chinese_tag'] = rowData.get('chinese_tag')
                item['comments_count'] = rowData.get('comments_count')
                yield item
            yield Request(url=self.url.format(behot_time=nextTime, behot_time_tmp=nextTime), callback=self.parse)
        else:
            logging.info("The Data is null")

# 作者：芒果DB
# 链接：http://www.jianshu.com/p/475f9f46c544
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。