# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class Fut19Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = Field()
    club = Field()
    ligue = Field()
    nationality = Field()
    name = Field()
    rating = Field()
    position = Field()
    pace = Field()
    shoot = Field()
    passe = Field()
    dribble = Field()
    defense = Field()
    physicist = Field()
    price = Field()
    compared_yesterday = Field()
    age = Field()
    height = Field()
    weight = Field()
    workrates = Field()
    foot = Field()
    phisical_info = Field()
    stats = Field()
