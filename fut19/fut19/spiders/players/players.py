# -*- coding: utf-8 -*-

import csv
import scrapy

from scrapy.http import Request

from fut19.items import Fut19Item, Fut19ItemStats, Fut19ItemPhysical
from fut19.loaders import Fut19Loader, Fut19LoaderPhysical, Fut19LoaderStats
from .constants import (XPATH_LINKS,
                        XPATH_PAGINATION,
                        XPATHS_PLAYER_INFO,
                        XPATHS_PHYSICAL_INFO,
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
        with open('example.csv', 'r') as f:
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
        loader_stats.add_xpaths(XPATHS_STATS_INFO)
        loader.add_value('stats', loader_stats.load_item())

        loader_physical = Fut19LoaderPhysical(
            Fut19ItemPhysical(), response.xpath(
                XPATHS_PLAYER_INFO['_physical_info']))
        loader_physical.add_xpaths(XPATHS_PHYSICAL_INFO)
        loader.add_value('physical_info', loader_physical.load_item())

        yield loader.load_item()


# with open('dump.html', 'wb') as f: f.write(response.body)