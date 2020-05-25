# -*- coding: utf-8 -*-
from car.items import CarItem
import scrapy
import json


class CarSpider(scrapy.Spider):
    name = 'cars1'
    allowed_domains = ['www.carsforsale.com', 'api.carsforsale.com']
    start_urls = ['https://www.carsforsale.com/Search?SearchTypeID=2&PageResultSize=50&PageNumber=1']
    # &Conditions=Used

    def parse(self, response):
        cars = response.xpath('//ul[@id="vehiclepage"]/li[contains(@class, "vehicle-results-snapshot")]')
        for car in cars:
            link = car.xpath('.//a[contains(@class, "vehicle-name")]/@href').extract_first()
            yield scrapy.Request(
                'https://api.carsforsale.com/api/Vehicle/Profile/Retrieve',
                callback=self.parse_url,
                method='POST',
                body=json.dumps({'VehicleID': link.replace('/vehicle/details/', ''), 'Radius': '1000', 'ExcludePriceAndImageHistory': 'false'}),
                headers={'Content-Type': 'application/json', 'Authorization': 'app_jzfq9zbugfrafizj eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJEYXRlVmFsaWQiOiJcL0RhdGUoMTU3NDk1MTY2Mjg0MClcLyIsIkNvbnRleHQiOnsiSWQiOjAsIkF2YXRhclVybCI6bnVsbCwiRmlyc3ROYW1lIjpudWxsLCJMYXN0TmFtZSI6bnVsbCwiRW1haWwiOm51bGwsIlR5cGUiOiJhbm9ueW1vdXMifSwiQXBwS2V5IjoiYXBwX2p6ZnE5emJ1Z2ZyYWZpemoiLCJBcGlLZXkiOiJhcGlfNno0c3N2bHRhMW8zYmc4MCIsIlRva2VuIjpudWxsLCJJZCI6MH0.kyz8MpmeM4f4biNnQYe1o_Csg9jvpRqC7DEYwzV9ZcY'}
            )
        next_page = response.xpath('//button[contains(@class, "btn-pagination-next")]/@data-page-number').extract_first()
        if next_page is not None:
            yield scrapy.Request('https://www.carsforsale.com/Search?SearchTypeID=2&PageResultSize=50&PageNumber='+next_page)

    @staticmethod
    def parse_url(response):
        data = json.loads(response.body_as_unicode())
        item = CarItem()
        for key, value in data.items():
            item[key] = value
        yield item
