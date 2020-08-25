# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:57:02 2020

@author: alexl
"""

import urllib.request, json, requests, sys
from bs4 import BeautifulSoup
    
def yuyuParse(url):
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
    
    return (cardDict)


# Create list of card id's
    
def main(argv):
    
    with urllib.request.urlopen("https://www.encoredecks.com/api/deck/1tq7PVTGc") as url:
         data = json.loads(url.read())
    
    card_id_list = []
    
    for i in range(len(data['cards'])):
        # print(data['cards'][i].get('set') + "/" + data['cards'][i].get('side') +
        #       data['cards'][i].get('release') + "-" + data['cards'][i].get('sid'))
        
        card_id_list.append(data['cards'][i].get('set') + "/" + data['cards'][i].get('side') +
               data['cards'][i].get('release') + "-" + data['cards'][i].get('sid'))
    print(card_id_list)
    
    # Get list of sets
    
    set_list = []

    
    for j in range (len(data['sets'])):
        set_list.append(data['cards'][j].get('set'))
        
    
    #Pass set urls to yuyuParse and compile all price dicts
    dict_collection = {}
    
    for set_id in set_list:
        url = "https://yuyu-tei.jp/game_ws/sell/sell_price.php?name=" + set_id.lower()
        priceDict = yuyuParse(url)
        dict_collection.update(priceDict)
        
    
    print(dict_collection)
    total = 0
    
    
    for card_id in card_id_list:
        total += dict_collection.get(card_id, 0)
        print(total)
    
    print("Your deck costs: " + str(total) + "円")
    


if __name__ == "__main__":
   main(sys.argv[1:])
    