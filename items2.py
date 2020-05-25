# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarItem2(scrapy.Item):
    StartTime = scrapy.Field()
    VehicleID = scrapy.Field()
    VIN = scrapy.Field()
    Make = scrapy.Field()
    Model = scrapy.Field()
    Year = scrapy.Field()
    Trim = scrapy.Field()
    Message = scrapy.Field()
    ExcludePriceAndImageHistory = scrapy.Field()
    FInventoryIDs = scrapy.Field()
    EVehicleIDs = scrapy.Field()
    Popularity = scrapy.Field()
    PopularityDescription = scrapy.Field()
    NationalPopularity = scrapy.Field()
    NationalPopularityDescription = scrapy.Field()
    DepreciationPrices = scrapy.Field()
    VehiclePriceHistory = scrapy.Field()
    Images = scrapy.Field()
    Price = scrapy.Field()
    RegionalAveragePrice = scrapy.Field()
    NationalAveragePrice = scrapy.Field()
    Mileage = scrapy.Field()
    RegionalAverageMileage = scrapy.Field()
    NationalAverageMileage = scrapy.Field()
    RegionalPriceDifference = scrapy.Field()
    NationalPriceDifference = scrapy.Field()
    RegionalMileageDifference = scrapy.Field()
    NationalMileageDifference = scrapy.Field()
    AverageDaysOnMarket = scrapy.Field()
    DaysOnMarket = scrapy.Field()
    RegionalCount = scrapy.Field()
    NationalCount = scrapy.Field()
    VehicleViews = scrapy.Field()
