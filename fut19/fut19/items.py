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
    price = Field()
    compared_yesterday = Field()
    workrates_info = Field()
    foot_info = Field()

    physical_info = Field()
    stats = Field()


class Fut19ItemStats(scrapy.Item):

    pace = Field()
    shoot = Field()
    passe = Field()
    dribble = Field()
    defense = Field()
    physicist = Field()


class Fut19ItemPhysical(scrapy.Item):

    age = Field()
    height = Field()
    weight = Field()
    workrates = Field()
    foot = Field()