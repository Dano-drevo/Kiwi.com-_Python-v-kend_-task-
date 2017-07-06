"""
This module is designed to get geographic coordinate system from location's english name.
It uses kiwi.com API named 'places'.
"""

import requests
import os
def places(destination):
    r = requests.get("https://api.skypicker.com/places?term=" + destination + "&locale=en&v=2")
    lst = r.json()
    cities = []
    for item in lst:
        if item["type"] == 2:  #we are interested only in the cities, not the airports
            cities.append(item)
    if cities == []:
        os.system('clear')
        print('You have to choose existing city with existing airport, otherways you will stay home.\nOr you can use AITA airport code.')
        return False
    population = 0
    for city in cities:
        try:
            if population < city['population']: #choosing city with greatest population by default
                result = city
                country = city['parentId']
        except:
            pass
    if population == 0:
        city = cities[0]
    coordinates = (result['lat'] ,result['lng'])
    coordinates = round(coordinates[0],2) , round(coordinates[1],2)
    coordinates = str(coordinates[0])+"-" + str(coordinates[1])+"-250km"
    return coordinates, country
