# -*- coding: utf-8 -*-

XPATH_LINKS = ('//tr[contains(@class, "table-row")]'
               '/td[contains(@class, "face")]/a/@href')

XPATH_PAGINATION = ('//div[contains(@class, "pagination")]'
                    '//div[contains(@class, "next")]//a/@href')

XPATHS_PLAYER_INFO = {
    '_title': '//div[@class="titleDetails"]',
    '_physical_info': '//div[@class="physicalInfo"]',
    'club': './/div[contains(@class, "col-4")][1]/a/text()',
    'ligue': './/div[contains(@class, "col-4")][2]/a/text()',
    'nationality': './/div[contains(@class, "col-4")][3]/a/text()',
    'name': '//div[contains(@class, "name")][1]/text()',
    'rating': '//div[contains(@class, "-rating")]/text()',
    'position': '//div[contains(@class, "-position")]/text()',
    'skills': 'count(//div[contains(@class, "left")]/div[@class="stars"]/*)',
    'weakfoot': 'count(//div[contains(@class, "right")]/div[@class="stars"]/*)',
    'quality': '//div[contains(@class, "card-19 card-19")]/@class',
    'price': '//span[@class="counter"]/text()',
    'compared_yesterday': '//span[@class="green"]/text()',
    'workrates_info': ('//div[@class="physicalInfo"]'
                       '//div[contains(@class, "col")][5]/text()[2]'),
    'foot_info': ('//div[@class="physicalInfo"]'
                  '//div[contains(@class, "col")][6]/text()[2]'),
}

XPATHS_STATS_INFO = {
    'pac': '//div[@class="card-19-attnum card-19-attnum1"]/text()',
    'sho': '//div[@class="card-19-attnum card-19-attnum2"]/text()',
    'pas': '//div[@class="card-19-attnum card-19-attnum3"]/text()',
    'dri': '//div[@class="card-19-attnum card-19-attnum4"]/text()',
    'defense': '//div[@class="card-19-attnum card-19-attnum5"]/text()',
    'phy': '//div[@class="card-19-attnum card-19-attnum6"]/text()',
}

XPATHS_PHYSICAL_INFO = {
    'age': './/div[contains(@class, "col")][1]/text()[2]',
    'height': './/div[contains(@class, "col")][3]/text()[2]',
    'weight': './/div[contains(@class, "col")][4]/text()[2]',
    'workrates': './/div[contains(@class, "col")][5]/text()[2]',
    'foot': './/div[contains(@class, "col")][6]/text()[2]'
}