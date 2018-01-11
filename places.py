"""
This module is designed to get geographic coordinate system from location's description entered by the user.
It used to use kiwi.com API named 'places', but now the 'locations' API is needed instead.
"""
import requests
import os
def places(destination,strng):
    url="https://api.skypicker.com/locations?term=" + destination + "&locale=en"#&location_types="+strng
    r = requests.get(url)
    lst = r.json()['locations']
    cities = []
    for item in lst:
        if item["type"] == strng:  #we are interested only in the cities, not the airports
            cities.append(item)
         
    if cities == []:
        os.system('clear')
        print('You have to choose existing city with existing airport, otherways you will stay home.\nOr you can use AITA airport code.')
        return False
    coordinates = (cities[0]['location']['lat'],cities[0]['location']['lon'])
    if strng=='airport':
        city_name, country_name = (cities[0]['city']['name'] , cities[0]['city']['country']['name'])
    elif strng=='city':
        city_name, country_name = (cities[0]['name'] , cities[0]['country']['name'])
    coordinates = round(coordinates[0],2) , round(coordinates[1],2)
    coordinates = str(coordinates[0])+"-" + str(coordinates[1])+'-100km'
    return coordinates, city_name, country_name
