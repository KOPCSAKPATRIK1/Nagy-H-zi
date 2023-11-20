from datetime import datetime
from termcolor import colored

def new_name(): 
    while True: 
        new_name = input("Add meg a nevet (0 kilép): ")
        if new_name == '0':
            return False
        elif new_name == "" or new_name.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
             return new_name

def new_date():
    while True:
            try:
                new_date = input("Add meg a dátumot (YYYY.MM.DD formátumban) (0 kilép): ")
                if new_date == '0':
                    return False
                else:
                    date_object = datetime.strptime(new_date, "%Y.%m.%d")
                    formatted_date = date_object.strftime("%Y.%m.%d")
                    return str(formatted_date)
            except ValueError:
                print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
           

def new_time():
     while True:
          try:
               new_time = input("Add meg az időt (HH:MM formátumban) (0 kilép): ")
               if new_time == '0':
                    return False
               else:
                    time_object = datetime.strptime(new_time, '%H:%M')
                    return str(time_object.time())
          except ValueError:
               print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")

def new_desc(): 
    while True: 
        new_desc = input("Add meg a leírást (0 kilép): ")
        if new_desc == '0':
            return False
        elif new_desc == "" or new_desc.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
             return new_desc
        
def new_place(): 
    while True: 
        new_place = input("Add meg a helyszínt (0 kilép): ")
        if new_place == '0': 
            return False
        elif new_place == "" or new_place.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
             return new_place
     