# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class Fut19Item(scrapy.Item):

    _id = Field()
    link = Field()
    club = Field()
    ligue = Field()
    nationality = Field()
    name = Field()
    rating = Field()
    position = Field()
    skills = Field()
    weakfoot = Field()
    quality = Field()
    price = Field()
    compared_yesterday = Field()
    workrates_info = Field()
    foot_info = Field()

    physical_info = Field()
    stats = Field()
    stats_details = Field()


class Fut19ItemStats(scrapy.Item):

    pac = Field()
    sho = Field()
    pas = Field()
    dri = Field()
    defense = Field()
    phy = Field()


class Fut19ItemPhysical(scrapy.Item):

    age = Field()
    height = Field()
    weight = Field()
    workrates = Field()
    foot = Field()