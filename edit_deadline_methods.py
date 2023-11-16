from deadline_class import Deadline
from termcolor import colored

def display_deadlines(deadlines_list: list[Deadline]):
    max_name_length = max(len(deadline.name) for deadline in deadlines_list)
    max_date_length = max(len(deadline.date) for deadline in deadlines_list)
    max_time_length = max(len(deadline.time) for deadline in deadlines_list)
    max_place_length = max(len(deadline.place) for deadline in deadlines_list)

    for index, deadline in enumerate(deadlines_list, start=1):
       print(f"{index}. {deadline.name:<{max_name_length + 5}}{deadline.date:<{max_date_length + 5}}{deadline.time:<{max_time_length + 5}}{deadline.place:<{max_place_length + 5}}{deadline.desc}")

def select(deadlines_list: list[Deadline]):
    while True:
            display_deadlines(deadlines_list)
            try:
                print("Melyiket szeretnéd választani? (0 kilép): ")
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

def edit(deadline: Deadline, data, index):
    if index == 0:
        deadline.name = data
    elif index == 1:
        deadline.date = data
    elif index == 2:
        deadline.time = data
    elif index == 3:
        deadline.place = data
    elif index == 4:
        deadline.desc = data
    print('siker')
    return


