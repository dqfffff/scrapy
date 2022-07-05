# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv

from itemadapter import ItemAdapter
import logging
import codecs
from openpyxl import Workbook


class JobPipeline:
    def __init__(self) -> None:
        # 打开文件，指定方式为写，利用第3个参数把csv写数据时产生的空行消除
        self.f = open("file.csv", "w")
        # 设置文件第一行的字段名，注意要跟spider传过来的字典key名称相同
        self.fieldnames = ['公司名称', '薪资',
                           '工作岗位', '要求工作经验', '要求学历',
                           '公司地址', '公司人数', '标签1', '标签2', '标签3', '招聘链接']
        self.writer = csv.writer(self.f, delimiter=',')
        self.writer.writerow(self.fieldnames)

    def process_item(self, item, spider):
        line = [
            item['company'], item['scalary'], item['jobs'], item['experiences'], item['degree'], item['work_address'],
            item['company_persion'], item['tag1'], item['tag2'], item['tag3'], item['url']
        ]
        self.writer.writerow(line)
        return item

    def close_spider(self, spider):
        # 关闭
        self.f.close()
