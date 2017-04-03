# -*- coding: utf8 -*-
# coding: utf8

import scrapy, locale
locale.setlocale(locale.LC_ALL, 'zh_TW.UTF-8') 

class DistrictsDemoSpider(scrapy.Spider):
    name = "districtsDemo"

    def start_requests(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't']
        urls = map(lambda x:("http://www.elections.gov.hk/dc2015/chi/summary%s.html" % x), alphabet)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        district18 = response.css('p.heading::text').extract_first()
        if district18 == "北區".decode('utf-8'):
            districtNum = response.css('td.contents tr .contents::text')[0::3].extract()
            districtName = response.css('td.contents tr .contents::text')[1::3].extract()
            districtPopulation = response.css('td.contents tr .contents::text')[2::3].extract()
        else:
            districtNum = response.css('td.contents > div::text').extract()
            districtName = response.css('td.contents tr .contents::text')[0::2].extract()
            districtPopulation = response.css('td.contents tr .contents::text')[1::2].extract()
        for i in range(len(districtNum)):
            yield {
                "districtNum": districtNum [i],
                "districtName": districtName[i],
                "districtPopulaton": locale.atoi(districtPopulation[i]),
                "district18": district18,
            }
 