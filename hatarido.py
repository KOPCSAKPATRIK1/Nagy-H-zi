from termcolor import colored
from datetime import datetime 
from hatarido_class import Hatarido
import new_deadline_methods
import edit_deadline_methods

def menu():
    while True:
        print(f"{colored('HATÁRIDŐNAPLÓ', 'white', 'on_blue')}\n"
                "[1] Új rekord létrehozása\n"
                "[2] Rekord módosítása\n"
                "[3] Rekord törlése\n"
                "[4] Rekordok listázása idő szerint\n"
                "[5] Név szerinti keresés\n"
                f"{colored('[9] Kilépés', 'blue', 'on_red')}")
        choose = input(f"\n{colored('->', 'white', 'on_green')}")
        if choose != '1' and choose != '2' and choose != '3' and choose != '4' and choose != '5' and choose != '9':
             print(f"{colored('Nincs ilyen opció!', 'white', 'on_red')}")
        else:
            return choose
    
def load_file():
    deadline_txt = open('hataridok.txt', 'rt', encoding='utf-8')
    adat = deadline_txt.read()
    adat_lista = adat.split("\n")
    try:
       deadlines_list = [Hatarido(*deadline.split('; ')) for deadline in adat_lista]
       deadline_txt.close()
       return deadlines_list
    except Exception as e:
        print(f'A fájl beolvasása során hiba történt: {e}')
        deadlines_list = []
        deadline_txt.close()
        return deadlines_list
    


def main(main_lista):
    deadlines_list = main_lista
    choose = menu()
    
    if choose == '9': #kilépés
            with open('output.txt', 'w', encoding='utf-8') as file:
                for deadline in deadlines_list:
                    file.write(f"{deadline.name}; {deadline.date}; {deadline.time}; {deadline.place}; {deadline.desc}\n")
            print(f"{colored('Viszlát!', 'blue', 'on_white')}")
            exit()
        
    if choose == '1': #létrehozás
        input_name = new_deadline_methods.new_name()
        if input_name == False:
            main(deadlines_list)
        input_date = new_deadline_methods.new_date()
        if input_date == False:
            main(deadlines_list)
        input_time = new_deadline_methods.new_time()
        if input_time == False:
            main(deadlines_list)
        input_place = new_deadline_methods.new_place()
        if input_place == False:
            main(deadlines_list)
        input_desc = new_deadline_methods.new_desc()
        if input_desc == False:
            main(deadlines_list)
        deadlines_list.append(Hatarido(
            input_name,
            input_date,
            input_time,
            input_place,
            input_desc
            ))
        print(colored('Sikeres létrehozás.', 'green', 'on_green'))
        main(deadlines_list)

    if choose == '2': #módosítás
        selected = edit_deadline_methods.select(deadlines_list)
        if selected == False:
            main(deadlines_list)
        else: 
            print(f"Kiválasztott elem: {selected.name}; {selected.date}; {selected.time}; {selected.place}; {selected.desc}")
            while True:
                print(f"{colored('Mit szeretnél változtatni? (0 kilép)', 'white', 'on_blue')}\n"
                        "[1] Név\n"
                        "[2] Dátum\n"
                        "[3] Idő\n"
                        "[4] Helyszín\n"
                        "[5] Leírás\n")
                choose = input(f"\n{colored('->', 'white', 'on_green')}")
                if choose != '1' and choose != '2' and choose != '3' and choose != '4' and choose != '5' and choose != '0':
                    print(f"{colored('Nincs ilyen opció!', 'white', 'on_red')}")
                else:
                    break
            if choose == '0':
                main(deadlines_list)
            elif choose == '1':
                input_name = new_deadline_methods.new_name()
                if input_name == False:
                    main(deadlines_list)
                edit_deadline_methods.edit(selected, input_name, int(choose) - 1)
            elif choose == '2':
                input_date = new_deadline_methods.new_date()
                if input_date == False:
                    main(deadlines_list)
                edit_deadline_methods.edit(selected, input_date, int(choose) - 1)
            elif choose == '3':
                input_time = new_deadline_methods.new_time()
                if input_time == False:
                    main(deadlines_list)
                edit_deadline_methods.edit(selected, input_time, int(choose) - 1)
            elif choose == '4':
                input_place = new_deadline_methods.new_place()
                if input_place == False:
                    main(deadlines_list)
                edit_deadline_methods.edit(selected, input_place, int(choose) - 1)
            elif choose == '5':
                input_desc = new_deadline_methods.new_desc()
                if input_desc == False:
                    main(deadlines_list)
                edit_deadline_methods.edit(selected, input_desc, int(choose) - 1)
        main(deadlines_list)    


 
    return

main_lista = load_file()      
main(main_lista)