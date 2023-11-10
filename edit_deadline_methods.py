from hatarido_class import Hatarido
import new_deadline_methods
from termcolor import colored

def select(deadlines_list: list[Hatarido]):
    while True:
            for index, deadline in enumerate(deadlines_list, start=1):
                print(f"{index}. {deadline.name}; {deadline.date}; {deadline.time}")
            try:
                print("Melyiket szeretnéd módosítani? (0 kilép): ")
                choose = input(f"\n{colored('->', 'white', 'on_green')}")
                choose = int(choose)

                if 1 <= choose <= len(deadlines_list):
                    selected = deadlines_list[choose-1]
                    return selected
                elif choose == 0:
                    return False
                else:
                    print("Érvénytelen választás. Kérlek válassz újra.")
            except ValueError:
                print("Érvénytelen bemenet. Kérlek válassz újra.")
            except IndexError:
                print("Nincs ilyen index az adott listában. Kérlek válassz újra.")
            except Exception as e:
                print(f"Hiba történt: {e}") 

def edit(deadline: Hatarido, data, index):
    if index == 0:
        deadline.name = data
    elif index == 0:
        deadline.date = data
    elif index == 0:
        deadline.time = data
    elif index == 0:
        deadline.place = data
    elif index == 0:
        deadline.desc = data
    print('siker')
    return

    
