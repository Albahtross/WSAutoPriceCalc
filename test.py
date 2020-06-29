# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:43:54 2020

@author: alexl
"""


from bs4 import BeautifulSoup
from lxml import html
import requests

page = requests.get('https://yuyu-tei.jp/game_ws/sell/sell_price.php?name=NGL')
tree = html.fromstring(page.content)
    
"""print(page.content)"""

soup = BeautifulSoup(page.content, 'html.parser')