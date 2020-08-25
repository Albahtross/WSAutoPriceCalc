# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:43:54 2020

@author: alexl
"""


from bs4 import BeautifulSoup
import requests
import csv

dict yuyuParse(url):

    # page = requests.get('https://yuyu-tei.jp/game_ws/sell/sell_price.php?name=&vers%5B%5D=dcvslbdc&vers%5B%5D=dcvslblb&rare=&type=&kizu=0')
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    cards = soup.find_all("li", {"class" : "card_unit"})


    cardDict = {}

"""Dictionary of card_id's and prices, currently only uses base prices"""

"""TODO: use Sale Prices and indicate whether or not there's a sale for a specific card (multiple values in dictionary)"""

for card_unit in cards:
    id = card_unit.find("p", {"class":"id"}).get_text().strip()
    price = card_unit.find("p", {"class":"price"}).get_text().strip()
    

    split = price.split("\n", 1)
    base_price = split[0]
    
    
    priceNoYen = int(base_price.replace("円", "")); 
    cardDict.update({id : priceNoYen})
    print(id, priceNoYen)
    
return (cardDict)
for card_id in cardDict:
    print (card_id, cardDict[card_id])

"""Write CSV"""

csv_file = "card_prices.csv"
csv_columns = ['card_id', 'price']
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, cardDict.keys())
        writer.writeheader()
        writer.writerow(cardDict)
except IOError:
    print("I/O error")
