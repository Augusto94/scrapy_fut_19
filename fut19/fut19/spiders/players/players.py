# -*- coding: utf-8 -*-

import csv
import scrapy

from scrapy.http import Request

from fut19.items import Fut19Item
from .constants import XPATH_LINKS, XPATH_PAGINATION, XPATHS_PLAYER


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
                # import ipdb; ipdb.set_trace()
                yield Request(
                    link[0],
                    callback=self.extract_info_player,
                    dont_filter=True
                )

    def extract_info_player(self, response):
        item = Fut19Item()
        
        item['_id'] = int(response.url.split('/')[-1])

        title = response.xpath(XPATHS_PLAYER['title'])
        item['club'] = title.xpath(XPATHS_PLAYER['club']).extract_first()
        item['ligue'] = title.xpath(XPATHS_PLAYER['ligue']).extract_first()
        item['nationality'] = title.xpath(XPATHS_PLAYER['nationality']).extract_first()

        item['name'] = response.xpath(XPATHS_PLAYER['name']).extract_first()
        item['rating'] = response.xpath(XPATHS_PLAYER['rating']).extract_first()
        item['position'] = response.xpath(XPATHS_PLAYER['position']).extract_first()
        item['price'] = response.xpath(XPATHS_PLAYER['price']).extract_first()
        item['compared_yesterday'] = response.xpath(XPATHS_PLAYER['compared_yesterday']).extract_first()
        item['stats'] = {
            'pace': response.xpath(XPATHS_PLAYER['pace']).extract_first(),
            'shoot': response.xpath(XPATHS_PLAYER['shoot']).extract_first(),
            'passe': response.xpath(XPATHS_PLAYER['passe']).extract_first(),
            'dribble': response.xpath(XPATHS_PLAYER['dribble']).extract_first(),
            'defense': response.xpath(XPATHS_PLAYER['defense']).extract_first(),
            'physicist': response.xpath(XPATHS_PLAYER['physicist']).extract_first(),
        }

        phisical_info = response.xpath(XPATHS_PLAYER['phisical_info'])
        item['phisical_info'] = {
            'age': phisical_info.xpath(XPATHS_PLAYER['age']).extract_first(),
            'height': phisical_info.xpath(XPATHS_PLAYER['height']).extract_first(),
            'weight': phisical_info.xpath(XPATHS_PLAYER['weight']).extract_first(),
            'workrates': phisical_info.xpath(XPATHS_PLAYER['workrates']).extract_first(),
            'foot': phisical_info.xpath(XPATHS_PLAYER['foot']).extract_first(),
        }

        yield item


# with open('dump.html', 'wb') as f: f.write(response.body)