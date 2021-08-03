#!/usr/bin/env python3


#PY 2: RICK AND MORTY API

import os
import datetime
import pyfiglet
from urllib.request import urlopen as url_open
import urllib
import json
#from PIL import Image

result = pyfiglet.figlet_format("XYZ X.Y")
print(result)
os.system("date")
print("\n") # describtion-row




def rmAPI_search(search_query):
    URL = 'https://rickandmortyapi.com/api/character/?name=' + search_query
    IRRELEVANT = ['episode', 'url', 'created', 'image']
    
    try:
        opened = url_open(URL).read().decode('utf-8')
        info_json = json.loads(opened)
        for result in info_json['results']: 

#'results' : [{'key': value}, {'key' : {'key': value}}] -> format of the json return from the API call

            for key in result:
                if key not in IRRELEVANT:
                    value = result[key]
                    if key == "origin" or key == "location":
                        value = result[key]['name']
                    try:
                        print('{}: {}'.format(key, value))
                        #Image.open(url_open(result['image']))
                    except:
                        value = value.encode('utf-8')
                        print('{}: {}'.format(key, value))
                        #Image.open(url_open(result['image']))
            print("\n")         
            
    except:
        print('{}: No such character found'.format(search_query))
    
rmAPI_search('morty')
