"""
This module represents functions and classes resposible for requesting valid inputs according to criteria of arguments.
"""
import os
import re
import datetime
from places import places
import time

#flight_data represents dictionary which will be used to get information about the flight
flight_data = {
'date':["(Enter date of the departure in 'YYYY-MM-DD' format.\nDon't forget that today is "+ time.strftime("%Y-%m-%d") +".\nIf you want to take off today, type 'now')\n",'Date'],
'from':["(Enter the preffered destination of your departure.)\n",'Airport'],
'to':["(Enter the preffered destination of your arrival.)\n",'Airport'],
'return':["(How many days are you wishing to stay in your destination?\nYou need to use integers only)\n",'Integer']
    }


#personal_data represents dictionary which will be used to get personal information about the passenger
personal_data = {
'email':['(Please enter your email address.)\n','Email'],
'gender':["(Enter your gender in 'm'/'f' format.)\n",'Gender'],
'first name':['What is your first name ?\n(Please enter only alphabetical letters.)\n','Name'],
'last name':['What is your last name ?\n(Please enter only alphabetical letters.)\n','Name'],
'birthday':['(Enter your birthday in YYYY-MM-DD format.)\n','Birthday'],
'id':["(Enter your ID/passport number. Don't make a mistake. It will be used for your authorization.)\n",'Id']
    }


class Id(): #ID/passport number authorization
    def __init__(self,doc_id):
        self.id = doc_id
    def validate(self):
        if len(self.id)  <= 4:
            print('This seems too short. Please recheck.\n')
            return False
        else:
            return True


class Integer(): #number of nights staying in destinaion authorization
    def __init__(self, integer):
        self.integer = integer
    def validate(self):
        try:
            self.integer = int(self.integer)
            return True
        except:
            return False


class Email(): #email authorization
    def __init__(self,email):
        self.email = email
    def validate(self):
        if ' ' not in self.email:
            if re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
                return True


class Gender(): #gender authorization
    def __init__(self, sex):
        self.gender = sex
    def validate(self):
        self.gender = self.gender.lower()
        if self.gender in ['m','f']:
            return True


class Name(): #name  authorization, method checks if the string is letter-only built
    def __init__(self,name):
        self.name = nice(name)
    def validate(self):
        return self.name.isalpha()


class Airport(Name): #IATA code authorization. However it checks only form of input, not actual existence of airport. If the user uses wrong IATA, he won't find anything.
    def __init__(self,name):
        self.airport = name
        super().__init__(name)
    def validate(self):
        if super().validate():
            if len(self.airport) == 3:
                return True


class Date(): #correct date format authorization
    def __init__(self, date):
        self.date = date
    def validate(self):
        try:
            self.date = datetime.datetime.strptime(self.date, '%Y-%m-%d')
            self.date = datetime.date(self.date.year, self.date.month, self.date.day).isoformat()
            return True
        except ValueError:
            return False


class Birthday(Date):#correct birthday date format authorization
    def __init__(self,date):
        super().__init__(date)
        self.birthday = date
    def validate(self):
        if super().validate():
            if int(self.date[:4]) <= 1900:
                print('You cannot be that old, please, set a valid birthday.')
            elif self.date >= time.strftime("%Y-%m-%d"):
                print('You cannot be that young, please, set a valid birthday.')
            else:
                self.birthday = datetime.datetime.strptime(self.birthday,'%Y-%m-%d').strftime('%Y-%m-%d')
                return True


def nice(text): #function which transformes complex words with white spaces into nice representation aka the first letters are  transformed to uppercase.
    if ' ' in text:
        text = text.split(' ')
        for txt in text:
            text[text.index(txt)] = txt[0].upper() + txt[1:]
        text = ' '.join(text)
    else:
        text = text[0].upper() + text[1:]
    return text



def destination(where): #function resposbile for finding and validating destination information. It's up to the user if he chooses searching according to IATA or name of the city.
    while True:
        print(where)
        a = input("Type 'a' for entereing destination IATA code.\nType 'b' for entering destination english name.\n")
        os.system('clear')
        if a.lower() in ['a','b']:
            if a.lower() == 'a':
                destination = input(where+'What airport is on your mind ?\n')
                destination = Airport(destination)
                if not destination.validate():
                    os.system('clear')
                    print('Your input is not IATA code.\n')
                    continue
                else:
                    destination = destination.name.upper()
                    break
            elif a.lower() == 'b':
                answer = input(where + 'What city is on your mind ?\n')
                destination = places(answer)  #here is used module places
                if not destination:
                    continue
                a = input("I have found "+nice(answer)+', '+destination[1]+".\nIs it correct? if yes, type 'y', if not, press any other key.\n\n")
                if a.lower() == 'y':
                    break
                os.system('clear')
                continue
        else:
            os.system('clear')
            print("You have to choose between 'a' and 'b'.\n")
            continue
    return destination  #if user searches with IATA code, function return IATA code. However, if user searchs according to the city name, function return tuple containing name of the city and home country




#The key function resposible for storing user inputs and validating them with classses methods.
def info(data,lst,dic):
    for key, value in data.items():
        while True:
            if key in lst: #in case of already entered opitonal argument,
                answer = dic[key]
                instance = eval(value[1])(answer)
            elif key in ['from','to']: #destination is specific, therfore it has special handling
                    value[0] = destination(value[0])
                    if not isinstance(value[0],tuple): #in case user searches according to the destination name
                            instance = Airport(value[1])
                    os.system('clear')
                    break
            else:
                answer = input(value[0])
                if (key == 'date') and (answer == 'now'):
                    answer = time.strftime("%Y-%m-%d")
                if answer == '':
                    os.system('clear')
                    continue
                instance = eval(value[1])(answer)
                os.system('clear')
            if instance.validate():
                break
            else:
                if key in lst:
                    lst.remove(key) #in case of wrong already entered optional argument
                print('You have entered an incorrect value. Try again.\n')
                continue
        if not isinstance(value[0],tuple):
            if instance.validate():
                value[0] = eval('instance.' + value[1].lower())
    return data #this returned object will be later used in searching for flight and booking it
