# Kiwi.com-_Python-v-kend_-task-
Task for a python challenge organized by KIWI.com

UPDATE:
--------
####################################################################
-------------------------------------------------------------------------------------------------------------------------------
The facts, that KIWI.com APIs depreciated and also KIWI.com booking_challenge has ended mean the booking server cannot be accessed and used anymore(book_flight.py) by this program e.i. it serves the original purpose no more. However, user can search for a ticket and program will provide him with the specific link to the merchant(https://www.kiwi.com/) webpage.
-------------------------------------------------------------------------------------------------------------------------------
Nevertheless, I've decided to keep this code alive and I also kept former lines and marked them as comments (#).
-----------------------------------------------------------------------------------------------------------------------------
The program as it is now will display only price of the flight, number of the stops between the takeoff and the landing, and will also provide user with a link to the webpage on which he is enabled to book a given flight.
####################################################################
-------------------------------------------------------------------------------------------------------------------------------

ABOUT:
Simple command line application for flight booking simulation using kiwi.com APIs.

"book_flight.py" is main program and it uses other ones as modules.
Execute with "--help" flag to display program usage shown below.
```
$python book_flight.py --help
```

```
>>>
usage: book_flight.py [-h] [-d DATE] [-f FROM] [-t TO] [-r RETURN] [-o] [-c]
                      [-s]

optional arguments:
  -h, --help            show this help message and exit
  -d DATE, --date DATE  Date of your flight, enter in YYYY-MM-DD format. You
                        can also enter 'now' for today's date.
  -f FROM, --from FROM  Departure destination. Please enter an airport IATA
                        code
  -t TO, --to TO        Arrival destination. Please enter an airport IATA code
  -r RETURN, --return RETURN
                        Number od nights spent in the arrival city.
  -o, --one-way         Indicates need of flight only to the location and not
                        back. (default)
  -c, --cheapest        Book the cheapest flight. (default)
  -s, --shortest        Book the shortest flight.
```

In order to start   "book_flight.py"   it's necesery to have modules  'flights.py',  'places.py'   and   'inputs.py'    in the same folder as 'book_flight.py'.
