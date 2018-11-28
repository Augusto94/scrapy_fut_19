# -*- coding: utf-8 -*-

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags

from fut19.utils import (count_stars,
                         parse_card,
                         parse_float,
                         parse_int,
                         string_digits_only)


class Fut19LoaderDefault(ItemLoader):

    default_output_processor = TakeFirst()
    
    def add_xpaths(self, fields, raw=None, re={}):
        """Método auxiliar para adicionar dict de campos ao loader.
        :fields: {campo1: xpath,
                  campo2: (xpath[, args[, kwargs]]),
                  ...}
        :raw: True                  # todos os campos
        :raw: [campo1, campo2, ...] # lista de campos
        """
        if raw:
            raw_fields = self.item.setdefault('raw', {})
        for field, args in fields.items():
            if not field or field.startswith('_'):
                continue

            args, kwargs = self._resolve_args(args)
            if field in re:
                kwargs.setdefault('re', re[field])

            self.add_xpath(field, *args, **kwargs)
            if raw is True or raw and field in raw:
                raw_value = self.get_xpath(args[0], Join())
                if raw_value:
                    raw_fields[field] = self.get_xpath(args[0], Join())

    def _resolve_args(self, args):
        kwargs = {}
        if not isinstance(args, tuple):
            args = (args,)
        elif isinstance(args[-1], dict):
            args, kwargs = args[:-1], args[-1]
        return args, kwargs


class Fut19Loader(Fut19LoaderDefault):

    price_in = MapCompose(parse_float)
    compared_yesterday_in = MapCompose(parse_float)
    rating_in = MapCompose(parse_int)
    skills_in = MapCompose(count_stars)
    weakfoot_in = MapCompose(count_stars)
    quality_in = MapCompose(parse_card)


class Fut19LoaderStats(Fut19Loader):

    default_input_processor = MapCompose(parse_int)


class Fut19LoaderPhysical(Fut19Loader):

    age_in = MapCompose(remove_tags, parse_int)
    height_in = MapCompose(remove_tags, string_digits_only, parse_float)
    weight_in = MapCompose(remove_tags, string_digits_only, parse_int)
