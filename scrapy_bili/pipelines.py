# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import codecs
import csv
import encodings


class ScrapyBiliPipeline:
    def __init__(self):
        self.file = codecs.open('a.csv', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # print("title:", item['title'])
        # print("url:", item['url'])
        fieldnames = ['id', 'title', 'url', 'up_time', 'play_count', 'like_count']
        w = csv.DictWriter(self.file, fieldnames=fieldnames)
        # w.writeheader()
        w.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()

