"""
Main part of the application. It's resposible for optional arguments and work with them.
Also with help of other modules, it executes all the process of finding, checking and booking a flight, ending with outputing PNR code.
"""
import os
import argparse
from inputs import *
from flights import *
import time
import json

#function resposible for creating a dictionary containing all the important valid information, which will be later used for booking process
def booking_data(dic):
    if dic['gender'][0].lower() == 'm':
        dic['title'] = 'Mr'
    else:
        dic["title"] = 'Mrs'
    data = {
                "passengers":[
                    {
                        "birthday":     dic['birthday'][0]+'12:00:10+00:00',
                        "firstName":    dic['first name'][0],
                        "lastName":     dic["last name"][0],
                        'documentID': dic["id"][0],
                        "title":    dic['title'],
                        "email":    dic["email"][0]
                    }
                ],
                "currency":         dic['currency'],
                "booking_token":    dic["booking_token"]
            }
    return data



#function that links all the funcionality of program together and returns confirmation of booking - PNR code
def book_the_flight():
    dic1 = info(flight_data,lst,dic) #first ditionary, resposible for flight attributes
    currency, booking_token = flights(dic1['from'][0], dic1['to'][0], dic1['date'][0], value, typeFlight, rt) #using flights module to find a wishing flight
    if (currency,booking_token) == ():
        system.os('clear')
        print('Something went wrong. Please try to use application once again.\n')
        return
    dic2 = info(personal_data,[],{}) #second dictionary ,resposible for customer information
    dic2['currency'] = currency
    dic2['booking_token'] = booking_token
    url = 'http://37.139.6.125:8080/booking'
    r = requests.post(url,headers={'content-type': 'application/json'}, data=json.dumps(booking_data(dic2))) #process of booking
    try:
        pnr = r.json()['pnr']
        print("Congratulations ! You've just booked your flight.\nThis is your PNR number:      '"+pnr+"'\nDon't lose it ;)") #final line of code, printing PNR number, which represents booked flight and job done
        return pnr
    except:
        system.os('clear')
        print('There might be some problem with the server. Please wait a little and try it again.\n')

#setting an enviroment for optional argument entering
parser = argparse.ArgumentParser()
parser.add_argument("-d","--date",help = "Date of your flight, enter in YYYY-MM-DD format. You can also enter 'now' for today's date.",type = str)
parser.add_argument("-f","--from",help = 'Departure destination. Please enter an airport IATA code',type = str)
parser.add_argument("-t","--to",help = 'Arrival destination. Please enter an airport IATA code',type = str)
parser.add_argument("-r","--return",help = 'Number od nights spent in the arrival city.',type = int)
parser.add_argument("-o","--one-way",help = 'Indicates need of flight only to the location and not back.\n(default)',action="store_true")
parser.add_argument("-c","--cheapest",help = 'Book the cheapest flight.\n(default)',action="store_true")
parser.add_argument("-s","--shortest",help = 'Book the shortest flight.',action="store_true")
args = parser.parse_args()
dic = vars(args)

#next lines of code are resposible for deciding which values will be used in program and what attributes should meet the wishing flight
dic['one-way'] = dic.pop('one_way')
if dic['date'] == 'now':
    dic["date"] = time.strftime("%Y-%m-%d")
if dic['return']==None:
    dic['one-way']=True
    flight_data.pop('return', None)
    rt = ''
else:
    dic['one-way']=False
    rt = "&daysInDestinationFrom="+str(dic['return'])+"&daysInDestinationTo="+str(dic['return'])
if dic['shortest']==False:
    dic['cheapest']=True
else:
    dic['cheapest']=False
lst = []
for key, item in dic.items():
    if item:
        lst.append(key)
if 'cheapest' in lst:
    value = 'price'
else:
    value = 'duration'
if 'one-way' in lst:
    typeFlight = 'oneway'
else:
    typeFlight = 'round'

pnr = book_the_flight()
