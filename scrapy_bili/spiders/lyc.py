import scrapy
# from pyquery.pyquery import callback

from scrapy_bili.items import ScrapyBiliItem


class LycSpider(scrapy.Spider):
    name = 'lyc'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/movie?from_spmid=666.7.hotlist.more']

    def parse(self, response):
        item = ScrapyBiliItem()
        for jobs_primary in response.xpath('//*[@id="app"]/div/div[2]/div[2]/ul/li'):
            item['id'] = jobs_primary.xpath('./div/div[1]/i/span/text()').get()         # 电影id
            item['title'] = jobs_primary.xpath('./div/div[2]/a/text()').get()           # 电影名称
            item['url'] = jobs_primary.xpath('./div/div[2]/a/@href').extract()[0][2:]   # 电影链接
            item['up_time'] = jobs_primary.xpath('./div/div[2]/div/span/text()'
                ).get().replace("\n", "").replace(" ", "")[:-2]  # 上映时间
            item['play_count'] = float(jobs_primary.xpath('./div/div[2]/div/div/span[1]/text()'
                ).get().replace("\n","").replace(" ", "")[:-1]) # 播放量
            item['like_count'] = float(jobs_primary.xpath('./div/div[2]/div/div/span[2]/text()'
                ).get().replace("\n", "").replace(" ", "")[:-1]) # 喜欢人数
            yield item
        # get other page, and parse again
        # url = response.request.url
        # new_link = url[0:-1] + str(int(url[-1]) + 1)
        # yield scrapy.Request(new_link, callback=self.parse)
# //*[@id="all-list"]/div[1]/ul/li[1]/a/div/div[3]