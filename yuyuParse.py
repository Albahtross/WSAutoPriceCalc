# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:43:54 2020

@author: alexl
"""


from bs4 import BeautifulSoup
from lxml import html
import requests

"""print(page.content)"""



page = requests.get('https://yuyu-tei.jp/game_ws/sell/sell_price.php?name=&vers%5B%5D=dcvslbdc&vers%5B%5D=dcvslblb&rare=&type=&kizu=0')

soup = BeautifulSoup(page.content, 'html.parser')


""" All cards"""

cards = soup.find_all("li", {"class" : "card_unit"})


"""TODO: Make an array, for each li with class = "card unit" get p class = "id",
and p class = "price" """



print(cards)
