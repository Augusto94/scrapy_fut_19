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

    div = Field()
    han = Field()
    kic = Field()
    ref = Field()
    spd = Field()
    pos = Field()


class Fut19ItemPhysical(scrapy.Item):

    age = Field()
    height = Field()
    weight = Field()
    workrates = Field()
    foot = Field()


class Fut19ItemStatsDetails(scrapy.Item):

    acceleration = Field()
    sprint_speed = Field()
    positioning = Field()
    finishing = Field()
    shot_power = Field()
    long_shots = Field()
    volleys = Field()
    penalties = Field()
    vision = Field()
    crossing = Field()
    fk_acc = Field()
    short_pass = Field()
    long_pass = Field()
    curve = Field()
    agility = Field()
    balance = Field()
    reactions = Field()
    ball_control = Field()
    dribbling = Field()
    composure = Field()
    interceptions = Field()
    heading_acc = Field()
    marking = Field()
    stand_tackle = Field()
    slide_tackle = Field()
    jumping = Field()
    stamina = Field()
    strength = Field()
    aggression = Field()

    gk_diving = Field()
    gk_handling = Field()
    gk_kicking = Field()
    gk_reflexes = Field()
    gk_pos = Field()