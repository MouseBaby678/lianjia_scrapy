import time

import scrapy
from lianjia.items import LianjiaItem

class LianjiaScrapySpider(scrapy.Spider):
    name = "lianjia_scrapy"
    allowed_domains = ["jn.lianjia.com"]
    start_urls = ["https://jn.lianjia.com/ershoufang/quanjingwolongqu/pg1/"]

    def parse(self, response):
        li_list = response.xpath('//*[@id="content"]/div[1]/ul/li')
        print(len(li_list))
        for li in li_list:
            item = LianjiaItem()
            item['title'] = li.xpath('./div[1]/div[1]/a/text()').extract_first()
            detail_url = li.xpath('./div[1]/div[1]/a/@href').extract_first()
            print(detail_url)
            time.sleep(1)
            yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={"item": item})
        pass

    def detail_parse(self, response):
        item = response.meta['item']
        item['totalprice'] = response.xpath('/html/body/div[5]/div[2]/div[3]/div/span[1]/text()').extract_first()
        item['unitprice'] = response.xpath('/html/body/div[5]/div[2]/div[3]/div/div[1]/div[1]/span/text()').extract_first()
        item['community'] = response.xpath('/html/body/div[5]/div[2]/div[5]/div[1]/a[1]/text()').extract_first()
        item['position'] = response.xpath('/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a[1]/text()').extract_first() + '-' + response.xpath('/html/body/div[5]/div[2]/div[5]/div[2]/span[2]/a[2]/text()').extract_first()
        fangwuhuxing_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[1]/text()').getall()
        fangwuhuxing_valid = [item.strip() for item in fangwuhuxing_list if item.strip()]
        fangwuhuxing = fangwuhuxing_valid[0] if fangwuhuxing_valid else None
        item['fangwuhuxing'] = fangwuhuxing

        louceng_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[2]/text()').getall()
        louceng_valid = [item.strip() for item in louceng_list if item.strip()]
        louceng = louceng_valid[0] if louceng_valid else None
        item['louceng'] = louceng

        jianzhumianji = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[3]/text()').getall()
        jianzhumianji_valid = [item.strip() for item in jianzhumianji if item.strip()]
        jianzhumianji = jianzhumianji_valid[0] if jianzhumianji_valid else None
        item['jianzhumianji'] = jianzhumianji

        huxingjiegou_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[4]/text()').getall()
        huxingjiegou_valid = [item.strip() for item in huxingjiegou_list if item.strip()]
        huxingjiegou = huxingjiegou_valid[0] if huxingjiegou_valid else None
        item['huxingjiegou'] = huxingjiegou

        taoneimianji_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[5]/text()').getall()
        taoneimianji_valid = [item.strip() for item in taoneimianji_list if item.strip()]
        taoneimianji = taoneimianji_valid[0] if taoneimianji_valid else None
        item['taoneimianji'] = taoneimianji

        jianzhuleixing_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[6]/text()').getall()
        jianzhuleixing_valid = [item.strip() for item in jianzhuleixing_list if item.strip()]
        jianzhuleixing = jianzhuleixing_valid[0] if jianzhuleixing_valid else None
        item['jianzhuleixing'] = jianzhuleixing

        fangwuchaoxiang_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()').getall()
        fangwuchaoxiang_valid = [item.strip() for item in fangwuchaoxiang_list if item.strip()]
        fangwuchaoxiang = fangwuchaoxiang_valid[0] if fangwuchaoxiang_valid else None
        item['fangwuchaoxiang'] = fangwuchaoxiang

        jianzhujiegou_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[8]/text()').getall()
        jianzhujiegou_valid = [item.strip() for item in jianzhujiegou_list if item.strip()]
        jianzhujiegou = jianzhujiegou_valid[0] if jianzhujiegou_valid else None
        item['jianzhujiegou'] = jianzhujiegou

        zhuangxiuqingkuang_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()').getall()
        zhuangxiuqingkuang_valid = [item.strip() for item in zhuangxiuqingkuang_list if item.strip()]
        zhuangxiuqingkuang = zhuangxiuqingkuang_valid[0] if zhuangxiuqingkuang_valid else None
        item['zhuangxiuqingkuang'] = zhuangxiuqingkuang

        louhubili_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[10]/text()').getall()
        louhubili_valid = [item.strip() for item in louhubili_list if item.strip()]
        louhubili = louhubili_valid[0] if louhubili_valid else None
        item['tihubili'] = louhubili

        gongnuanfangshi_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[11]/text()').getall()
        gongnuanfangshi_valid = [item.strip() for item in gongnuanfangshi_list if item.strip()]
        gongnuanfangshi = gongnuanfangshi_valid[0] if gongnuanfangshi_valid else None
        item['gongnuanfangshi'] = gongnuanfangshi

        peibeidianti_list = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[12]/text()').getall()
        peibeidianti_valid = [item.strip() for item in peibeidianti_list if item.strip()]
        peibeidianti = peibeidianti_valid[0] if peibeidianti_valid else None
        item['peibeidianti'] = peibeidianti

        item['guapaishijian'] = response.xpath('//*[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/span[2]/text()').extract_first()
        print(item)
        time.sleep(1)
        pass