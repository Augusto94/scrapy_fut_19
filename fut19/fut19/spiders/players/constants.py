# -*- coding: utf-8 -*-

XPATH_LINKS = ('//tr[contains(@class, "table-row")]'
               '/td[contains(@class, "face")]/a/@href')

XPATH_PAGINATION = ('//div[contains(@class, "pagination")]'
                    '//div[contains(@class, "next")]//a/@href')

XPATHS_PLAYER = {
    'title': '//div[@class="titleDetails"]',
    'club': './/div[contains(@class, "col-4")][1]/a/text()',
    'ligue': './/div[contains(@class, "col-4")][2]/a/text()',
    'nationality': './/div[contains(@class, "col-4")][3]/a/text()',
    'name': '//div[contains(@class, "name")][1]/text()',
    'rating': '//div[contains(@class, "-rating")]/text()',
    'position': '//div[contains(@class, "-position")]/text()',
    'pace': '//div[@class="card-19-attnum card-19-attnum1"]/text()',
    'shoot': '//div[@class="card-19-attnum card-19-attnum2"]/text()',
    'passe': '//div[@class="card-19-attnum card-19-attnum3"]/text()',
    'dribble': '//div[@class="card-19-attnum card-19-attnum4"]/text()',
    'defense': '//div[@class="card-19-attnum card-19-attnum5"]/text()',
    'physicist': '//div[@class="card-19-attnum card-19-attnum6"]/text()',
    'price': '//span[@class="counter"]/text()',
    'compared_yesterday': '//span[@class="green"]/text()',
    'phisical_info': '//div[@class="physicalInfo"]',
    'age': './/div[contains(@class, "col")][1]/text()[2]',
    'height': './/div[contains(@class, "col")][3]/text()[2]',
    'weight': './/div[contains(@class, "col")][4]/text()[2]',
    'workrates': './/div[contains(@class, "col")][5]/text()[2]',
    'foot': './/div[contains(@class, "col")][6]/text()[2]'
}
