from datetime import datetime
from termcolor import colored

def new_name():
    """
    Bekéri és visszaadja az új nevet a felhasználótól.

    Returns:
        str or bool: Az új név vagy False, ha a felhasználó kilépett.

    Usage:
        A függvény az új nevet kéri be a felhasználótól. 
        Ha a felhasználó 0-t ad meg, akkor kilép, egyébként az adott nevet adja vissza.
        Üres vagy csak szóközökből álló bemenetet elutasít, és hibát jelez a felhasználónak.
    """ 
    while True: 
        new_name = input("Add meg a nevet (0 kilép): ")
        if new_name == '0':
            return False
        elif new_name == "" or new_name.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
            return new_name

def new_date():
    """
    Bekéri és visszaadja az új dátumot a felhasználótól.

    Returns:
        str or bool: Az új dátum (formázott string) vagy False, ha a felhasználó kilépett.

    Usage:
        A függvény az új dátumot kéri be a felhasználótól a "YYYY-MM-DD" formátumban.
        Ha a felhasználó 0-t ad meg, akkor kilép, egyébként az adott dátumot adja vissza formázott stringként.
        Hibás formátum esetén figyelmeztet és újra bekéri az adatot.
    """
    while True:
            try:
                new_date = input("Add meg a dátumot (YYYY-MM-DD formátumban) (0 kilép): ")
                if new_date == '0':
                    return False
                else:
                    date_object = datetime.strptime(new_date, "%Y-%m-%d")
                    formatted_date = date_object.strftime("%Y-%m-%d")
                    return formatted_date
            except ValueError:
                print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
           

def new_time():
    """
    Bekéri és visszaadja az új időpontot a felhasználótól.

    Returns:
        str or bool: Az új időpont (formázott string) vagy False, ha a felhasználó kilépett.

    Usage:
        A függvény az új időpontot kéri be a felhasználótól a "HH:MM" formátumban.
        Ha a felhasználó 0-t ad meg, akkor kilép, egyébként az adott időpontot adja vissza formázott stringként.
        Hibás formátum esetén figyelmeztet és újra bekéri az adatot.
    """
    while True:
        try:
            new_time = input("Add meg az időt (HH:MM formátumban) (0 kilép): ")
            if new_time == '0':
                return False
            else:
                time_object = datetime.strptime(new_time, '%H:%M')
                formatted_time = time_object.strftime('%H:%M')
                return formatted_time
        except ValueError:
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")

def new_desc():
    """
    Bekéri és visszaadja az új leírást a felhasználótól.

    Returns:
        str or bool: Az új leírás vagy False, ha a felhasználó kilépett.

    Usage:
        A függvény az új leírást kéri be a felhasználótól. 
        Ha a felhasználó 0-t ad meg, akkor kilép, egyébként az adott leírást adja vissza.
        Üres vagy csak szóközökből álló bemenetet elutasít, és hibát jelez a felhasználónak.
    """
    while True: 
        new_desc = input("Add meg a leírást (0 kilép): ")
        if new_desc == '0':
            return False
        elif new_desc == "" or new_desc.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
             return new_desc
        
def new_place():
    """
    Bekéri és visszaadja az új helyszínt a felhasználótól.

    Returns:
        str or bool: Az új helyszín vagy False, ha a felhasználó kilépett.

    Usage:
        A függvény az új helyszínt kéri be a felhasználótól. 
        Ha a felhasználó 0-t ad meg, akkor kilép, egyébként az adott helyszínt adja vissza.
        Üres vagy csak szóközökből álló bemenetet elutasít, és hibát jelez a felhasználónak.
    """
    while True: 
        new_place = input("Add meg a helyszínt (0 kilép): ")
        if new_place == '0': 
            return False
        elif new_place == "" or new_place.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
             return new_place
     