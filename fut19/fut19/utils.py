# -*- coding: utf-8 -*-

import re


def parse_float(text):
    return float(text.replace(',', ''))


def parse_int(text):
    return int(text)


def string_digits_only(text):
    if not text:
        return None
    return u''.join(re.findall(r'\d+', text))


def count_stars(text):
    return int(text.split('.')[0])


def parse_card(text):
    return text.split('-')[-1]


def parse_rating_name(text):
    return text.replace('.', '').replace(' ', '_').lower()


def parse_strip(text):
    return text.strip()