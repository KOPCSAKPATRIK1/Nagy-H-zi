from deadline_class import Deadline
from termcolor import colored
import display_deadline_methods

def select(deadlines_list: list[Deadline]):
    while True:
            display_deadline_methods.display_deadlines(deadlines_list)
            try:
                print(colored('Melyiket szeretnéd választani? (0 kilép)', 'white', 'on_blue'))
                
                choose = input(f"\n{colored('->', 'white', 'on_green')}")
                choose = int(choose)

                if 1 <= choose <= len(deadlines_list):
                    selected = deadlines_list[choose-1]
                    return selected
                elif choose == 0:
                    return False
                else:
                    print(colored('Érvénytelen választás. Kérlek válassz újra.', 'white', 'on_red'))
            except ValueError:
                print(colored('Érvénytelen bemenet. Kérlek válassz újra.', 'white', 'on_red'))

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


