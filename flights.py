"""
This module is designed to get and work with raw flights data using kiwi.com API 'flights'.
It is needed to get essential information for booking a flight.
"""
import requests
import datetime
from pprint import pprint as pp

def where(coordinates):  #As we can search according to the place location or IATA airport code, this function decides what format is appropriate
    if isinstance(coordinates, tuple):
        return coordinates[0]
    else:
        return coordinates

def flights(from_coordinates, to_coordinates, date, value, typeFlight,rt): #Function flights() takes 5 positional arguments: departure place, arrival place, date of flying and flight attributes as sorting
                                                                           #priority and flightType(round/oneway).
    dt = str(date[8:10])+"%2F"+str(date[5:7])+"%2F"+str(date[:4])
    while True:
        url = "https://api.skypicker.com/flights?flyFrom="+ where(from_coordinates) +"&to="+ where(to_coordinates) +"&dateFrom="+dt+"&dateTo="+dt+rt+"&typeFlight="+typeFlight+"&partner=picky&partner_market=us&limit=1&sort="+value
        r = requests.get(url)
        flights = r.json()
        currency = flights['currency']
        data = flights["data"]
        number_of_stops=str(len(data[0]['route'])-1)
        goal_destination=data[0]['route'][~0]['cityTo']
        print("Your ticket will cost "+str(data[0]['conversion'][currency])+" "+currency+" and you have to take "+number_of_stops+" stops before arriving to "+goal_destination+".\n")
        print("\nHere is official link on which you can book the flight.\n")
        print(data[0]['deep_link']+"\n\n\nHappy journey :)\n")	
        #
        #This is the end of the program as some of KIWI.com APIs depreciated and also KIWI.com booking_challenge 
        #has ended and thus also booking server cannot be accessed and used anymore(gook_flight.py) by this program.
	#
        #The program will display price of the flight, number of the stops between the takeoff and the landing, and will
        #also provide user with a link to the webpage on which he is enabled to book a given flight.
        #
        no_longer_needed='''
        for flight in data:
            try:
                booking_token = flight["booking_token"]
                tup = (currency, booking_token)
            except:
                pass #nevhodny/neaktualny dataset
        if data == []:
            if flights["_results"] == 0:
                print("I'm sorry but no such flight was found.\nTry again.")
                tup = ()
                break
        else:
            break
    return tup #function returns tuple containing 'currency' and 'booking_token', 2 necessery items for process of booking
'''
        break
