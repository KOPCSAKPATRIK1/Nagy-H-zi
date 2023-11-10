from datetime import datetime
from termcolor import colored

def new_name(): 
    while True: 
        new_name = input("Add meg a nevet: ")
        if new_name == "" or new_name.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
             return new_name

def new_date():
    while True:
            try:
                input_date = input("Add meg a dátumot (YYYY.MM.DD formátumban): ")
                date_object = datetime.strptime(input_date, "%Y.%m.%d")
                return date_object.date()                
            except ValueError:
                print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
           

def new_time():
     while True:
          try:
               input_time = input("Add meg az időt (HH:MM formátumban): ")
               time_object = datetime.strptime(input_time, '%H:%M')
               return time_object.time()
          except ValueError:
               print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")

def new_desc(): 
    while True: 
        new_desc = input("Add meg a leírást: ")
        if new_desc == "" or new_desc.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
             return new_desc
        
def new_place(): 
    while True: 
        new_place = input("Add meg a helyszínt: ")
        if new_place == "" or new_place.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
             return new_place
     