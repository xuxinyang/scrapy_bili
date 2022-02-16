import scrapy
# from pyquery.pyquery import callback

from scrapy_bili.items import ScrapyBiliItem


class LycSpider(scrapy.Spider):
    name = 'lyc'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/movie?from_spmid=666.7.hotlist.more']

    def parse(self, response):
        item = ScrapyBiliItem()
        for jobs_primary in response.xpath('//*[@id="app"]/div/div[2]'):
            item['title'] = jobs_primary.xpath('./a/@title').extract()
            item['url'] = jobs_primary.xpath('./a/@href').extract()
            yield item

        url = response.request.url
        new_link = url[0:-1] + str(int(url[-1]) + 1)
        yield scrapy.Request(new_link, callback=self.parse)
