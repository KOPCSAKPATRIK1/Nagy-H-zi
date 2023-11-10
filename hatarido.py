from termcolor import colored
from datetime import datetime 
from hatarido_class import Hatarido
import letrehozas_methods

def menu():
    while True:
        print(f"{colored('HATÁRIDŐNAPLÓ', 'white', 'on_blue')}\n"
                "[1] Új rekord létrehozása\n"
                "[2] Rekord módosítása\n"
                "[3] Rekord törlése\n"
                "[4] Rekordok listázása idő szerint\n"
                "[5] Név szerinti keresés\n"
                "[6] Fáljba mentés, fáljból töltésˇ\n"
                f"{colored('[9] Kilépés', 'blue', 'on_red')}")
        choose = input(f"\n{colored('->', 'white', 'on_green')}")
        if choose != '1' and choose != '2' and choose != '3' and choose != '4' and choose != '5' and choose != '6' and choose != '9':
             print(f"{colored('Nincs ilyen opció!', 'white', 'on_red')}")
        else:
            return choose
    
def load_file():
    deadline_txt = open("hataridok.txt", "rt", encoding="utf-8")
    adat = deadline_txt.read()
    adat_lista = adat.split("\n")
    deadline_txt.close()
    return adat_lista

def main():
    deadlines_list = [Hatarido(*deadline.split('; ')) for deadline in load_file()]

    choose = menu()
    
    if choose == '9': #kilépés
            print(f"{colored('Viszlát!', 'blue', 'on_white')}")
            exit()
        
    if choose == '1': #létrehozás
        input_name = letrehozas_methods.new_name()
        input_date = letrehozas_methods.new_date()
        input_time = letrehozas_methods.new_time()
        input_place = letrehozas_methods.new_place()
        input_desc = letrehozas_methods.new_desc()
        deadlines_list.append(Hatarido(
            input_name,
            input_date,
            input_time,
            input_place,
            input_desc
            ))
        print(colored('Sikeres létrehozás.', 'green', 'on_green'))
        menu()

    if choose == '2': #módosítás
         pass

    return
            
main()