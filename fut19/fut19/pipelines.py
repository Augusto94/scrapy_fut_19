# -*- coding: utf-8 -*-

import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class Fut19Pipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):

    collection_name = 'players_fut'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'players')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item_player = dict(item)
        if self.db[self.collection_name].find({'_id': item_player['_id']}).count() != 0:
            del item_player['_id']
            self.db[self.collection_name].update({'_id': dict(item)['_id']}, {"$set": item_player}, upsert=False)
        else:
            self.db[self.collection_name].insert_one(item_player)
            log.msg("Player added to MongoDB database!", 
                level=log.DEBUG, spider=spider)

        return item
