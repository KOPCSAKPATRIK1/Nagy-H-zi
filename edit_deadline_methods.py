from deadline_class import Deadline
from termcolor import colored
import display_deadline_methods

def select(deadlines_list: list[Deadline]):
    """
    Kiválaszt egy határidőt a megadott listából vagy lehetőséget ad a kilépésre.

    Args:
        deadlines_list (List[Deadline]): Egy Deadline objektumokat tartalmazó lista.

    Returns:
        Union[Deadline, bool]: A kiválasztott határidő objektum, ha a felhasználó választott,
        vagy False, ha a felhasználó kilépett.

    Usage:
        A felhasználó a határidők listájából választhat egyet, vagy kiléphet az 0-val.
    """
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
    """
    Módosítja a megadott határidő objektum attribútumait az index alapján a kapott adatokkal.

    Args:
        deadline (Deadline): A módosítandó határidő objektum.
        data: Az új adat, amivel frissíteni szeretnénk az adott attribútumot.
        index (int): Az attribútumot jelölő index. 
            0: név, 1: dátum, 2: idő, 3: hely, 4: leírás.

    Returns:
        None

    Usage:
        A függvény segítségével lehet egy adott határidő objektum attribútumait módosítani.
    """
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


