# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()  # 公司名称
    scalary = scrapy.Field()  # 薪资
    jobs = scrapy.Field()  # 工作岗位
    experiences = scrapy.Field()  # 要求工作经验
    degree = scrapy.Field()  # 要求学历
    work_address = scrapy.Field()  # 公司地址
    company_persion = scrapy.Field()  # 公司人数
    tag1 = scrapy.Field()   # 标签
    tag2 = scrapy.Field()   # 标签
    tag3 = scrapy.Field()   # 标签
    # financing_condition = scrapy.Field()  # 融资情况
    url = scrapy.Field()  # 招聘链接
