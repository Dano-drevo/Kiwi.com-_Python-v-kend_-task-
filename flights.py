"""
This module is designed to get and work with raw flights data using kiwi.com API 'flights'.
It is needed to get essential information for booking a flight.
"""
import requests
import datetime
def flights(from_coordinates, to_coordinates, date, value, typeFlight,rt): #function flights() takes 5 positional arguments: departure place, arrival place, date of flying and flight attributes as sorting priority and flightType(round/oneway)
    dt = str(date[8:10])+"%2F"+str(date[5:7])+"%2F"+str(date[:4])
    while True:
        url = "https://api.skypicker.com/flights?flyFrom="+ where(from_coordinates) +"&to="+ where(to_coordinates) +"&dateFrom="+dt+"&dateTo="+dt+rt+"&typeFlight="+typeFlight+"&partner=picky&partner_market=us&limit=1&sort="+value
        r = requests.get(url)
        flights = r.json()
        currency = flights['currency']
        data = flights["data"]
        destinations = []
        for flight in data:
            try:
                booking_token = flight["booking_token"]
            except:
                pass #nevhodny/neaktualny dataset
        if data == {}:
            if r.json()["_results"] == 0:
                print("I'm sorry but no such flight was found.\nTry again.")
                tup = ()
                break
        else:
            tup = (currency, booking_token)
            break
    return tup #function returns tuple containing 'currency' and 'booking_token', 2 necessery items for process of booking

def where(coordinates):  #As we can search according to the place location or IATA airport code, this function decides what format is appropriate
    if isinstance(coordinates, tuple):
        return coordinates[0]
    else:
        return coordinates
