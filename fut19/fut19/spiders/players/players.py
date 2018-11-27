# -*- coding: utf-8 -*-

import csv
import scrapy

from scrapy.http import Request

from .constants import XPATH_LINKS, XPATH_PAGINATION


class PlayersSpider(scrapy.Spider):
    name = 'players'
    allowed_domains = 'https://www.futwiz.com'
    start_urls = ['https://www.futwiz.com/en/fifa19/players?page=0']

    def parse(self, response):
        # import ipdb; ipdb.set_trace()
        links_players = response.xpath(XPATH_LINKS).extract()
        for link in links_players:
            with open('url_players.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow([self.allowed_domains + link])
            # yield Request(
            #     self.allowed_domains + link,
            #     callback=self.extract_info_player,
            #     dont_filter=True
            # )
    
        next_page = response.xpath(XPATH_PAGINATION).extract_first()
        if next_page:
            yield Request(
                self.allowed_domains + next_page,
                callback=self.parse,
                dont_filter=True
            )
    
    def extract_info_player(self, response):
        with open('url_players.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile)
                spamwriter.writerow([response.url])


# with open('dump.html', 'wb') as f: f.write(response.body)