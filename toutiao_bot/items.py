import scrapy

class News(scrapy.Item):
	title = scrapy.Field()
	tag = scrapy.Field()
	label = scrapy.Field()
	chinese_tag = scrapy.Field()
	comments_count = scrapy.Field()
