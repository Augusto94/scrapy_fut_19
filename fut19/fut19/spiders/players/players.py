# -*- coding: utf-8 -*-

import csv
import scrapy

from scrapy.http import Request

from fut19.items import (Fut19Item,
                         Fut19ItemPhysical,
                         Fut19ItemStats,
                         Fut19ItemStatsDetails)
from fut19.loaders import (Fut19Loader,
                           Fut19LoaderPhysical,
                           Fut19LoaderStats,
                           Fut19LoaderStatsDetails)
from fut19.utils import parse_rating_name
from .constants import (XPATH_LINKS,
                        XPATH_PAGINATION,
                        XPATHS_PLAYER_INFO,
                        XPATHS_PHYSICAL_INFO,
                        XPATHS_STATS_INFO_GK,
                        XPATHS_STATS_DETAILS,
                        XPATHS_STATS_INFO)


class PlayersSpider(scrapy.Spider):
    name = 'players'
    allowed_domains = 'https://www.futwiz.com'
    start_urls = ['https://www.futwiz.com/en/fifa19/players?page=0']

    # def parse(self, response):
    #     # import ipdb; ipdb.set_trace()
    #     links_players = response.xpath(XPATH_LINKS).extract()
    #     for link in links_players:
    #         with open('url_players.csv', 'a') as csvfile:
    #             spamwriter = csv.writer(csvfile)
    #             spamwriter.writerow([self.allowed_domains + link])
    #         yield Request(
    #             self.allowed_domains + link,
    #             callback=self.extract_info_player,
    #             dont_filter=True
    #         )

    #     next_page = response.xpath(XPATH_PAGINATION).extract_first()
    #     if next_page:
    #         yield Request(
    #             self.allowed_domains + next_page,
    #             callback=self.parse,
    #             dont_filter=True
    #         )
    
    def parse(self, response):
        with open('url_players.csv', 'r') as f:
            links = csv.reader(f)
            for link in links:
                yield Request(
                    link[0],
                    callback=self.extract_info_player,
                    dont_filter=True
                )

    def extract_info_player(self, response):
        loader = Fut19Loader(Fut19Item(), response)

        loader.add_value('_id', int(response.url.split('/')[-1]))
        loader.add_value('link', response.url)

        loader.add_xpaths(XPATHS_PLAYER_INFO)

        loader_stats = Fut19LoaderStats(Fut19ItemStats(), response)
        if response.xpath(XPATHS_PLAYER_INFO['position']).extract_first() == "GK":
            loader_stats.add_xpaths(XPATHS_STATS_INFO_GK)
        else:
            loader_stats.add_xpaths(XPATHS_STATS_INFO)

        loader.add_value('stats', loader_stats.load_item())

        loader_physical = Fut19LoaderPhysical(
            Fut19ItemPhysical(), response.xpath(
                XPATHS_PLAYER_INFO['_physical_info']))
        loader_physical.add_xpaths(XPATHS_PHYSICAL_INFO)
        loader.add_value('physical_info', loader_physical.load_item())

        ratings_row = response.xpath(XPATHS_STATS_DETAILS['_row'])
        rating_details = []
        loader_stats = Fut19LoaderStatsDetails(Fut19ItemStats(), response)
        for rating_table in ratings_row:
            rating_field = rating_table.xpath(
                XPATHS_STATS_DETAILS['title']).extract_first().lower()
            if rating_field == 'def':
                rating_field = 'defense'

            for idx, rating in enumerate(rating_table.xpath(XPATHS_STATS_DETAILS['_tables'])):
                if idx == 0:
                    loader_status_details = Fut19LoaderStatsDetails(
                        Fut19ItemStatsDetails(), response)

                rating_name = rating.xpath(
                    XPATHS_STATS_DETAILS['rating']).extract_first()
                rating_value = rating.xpath(
                    XPATHS_STATS_DETAILS['rating_value']).extract_first()
                rating_name = parse_rating_name(rating_name)

                loader_status_details.add_value(rating_name, rating_value)

            loader_stats.add_value(
                rating_field, loader_status_details.load_item())

        loader.add_value('stats_details', [loader_stats.load_item()])

        yield loader.load_item()


# with open('dump.html', 'wb') as f: f.write(response.body)