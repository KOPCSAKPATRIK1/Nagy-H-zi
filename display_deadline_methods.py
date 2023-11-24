from deadline_class import Deadline
from datetime import datetime, timedelta
from termcolor import colored

def display_deadlines(deadlines_list: list[Deadline]):
    """
    Megjeleníti a határidőket egy táblázatos formában a konzolon.

    Args:
        deadlines_list (list[Deadline]): A megjelenítendő határidők listája.

    Returns:
        None

    Usage:
        A függvény a határidők adatait írja ki formázottan a konzolra.
    """
    max_name_length = max(len(deadline.name) for deadline in deadlines_list)
    max_place_length = max(len(deadline.place) for deadline in deadlines_list)
    sorted_deadlines = sorted(deadlines_list, key=lambda x: x.date)

    for index, deadline in enumerate(sorted_deadlines, start=1):
        print(f"{index}. {deadline.name:<{max_name_length + 5}}{deadline.date}    {deadline.time}     {deadline.place:<{max_place_length + 5}}{deadline.desc}")

def display_today(deadlines_list: list[Deadline]):
    """
    Megjeleníti a mai napon esedékes határidőket a konzolon.

    Args:
        deadlines_list (list[Deadline]): A határidők listája, amelyben keresi a mai napon esedékes határidőket.

    Returns:
        None

    Usage:
        A függvény az adott napon esedékes határidőket jeleníti meg formázottan a konzolra.
        Ha nincs ma határidő, akkor ezt jelzi a felhasználónak.
    """
    today = datetime.today().date()
    
    today_deadlines = [deadline for deadline in deadlines_list if deadline.date == today]
    if not today_deadlines:
        print(colored('Nincs ma határidő!', 'white', 'on_red'))
    else:
        today_deadlines.sort(key=lambda deadline: deadline.time)
        display_deadlines(today_deadlines)

def display_this_week(deadlines_list):
    """
    Megjeleníti az aktuális héten esedékes határidőket a konzolon.

    Args:
        deadlines_list (list): A határidők listája, amelyben keresi az aktuális héten esedékes határidőket.

    Returns:
        None

    Usage:
        A függvény az aktuális héten esedékes határidőket jeleníti meg formázottan a konzolra.
        Ha nincs ilyen határidő, akkor ezt jelzi a felhasználónak piros háttéren fehér szöveggel.
    """
    today = datetime.today().date()
    end_of_week = today + timedelta(days=(6 - today.weekday()))

    # Határidők szűrése az aktuális hétben és az aktuális hónapban
    this_week_deadlines = [
        deadline for deadline in deadlines_list 
        if today <= deadline.date <= end_of_week and deadline.date.month == today.month
    ]

    if not this_week_deadlines:
        print(colored('Nincs határidő aktuális héten!', 'white', 'on_red'))
    else:
        this_week_deadlines.sort(key=lambda deadline: deadline.date)
        display_deadlines(this_week_deadlines)

def display_remaining_month(deadlines_list):
    """
    Megjeleníti az aktuális hónapban esedékes határidőket a konzolon.

    Args:
        deadlines_list (list): A határidők listája, amelyben keresi az aktuális hónapban esedékes határidőket.

    Returns:
        None

    Usage:
        A függvény az aktuális hónapban esedékes határidőket jeleníti meg formázottan a konzolra.
        Ha nincs ilyen határidő, akkor ezt jelzi a felhasználónak piros háttéren fehér szöveggel.
    """
    today = datetime.today().date()
    end_of_month = today.replace(day=1, month=today.month+1) - timedelta(days=1)

    remaining_month_deadlines = [
        deadline for deadline in deadlines_list 
        if today <= deadline.date <= end_of_month
    ]

    if not remaining_month_deadlines:
        print(colored('Nincs határidő a hónapban!', 'white', 'on_red'))
    else:
        remaining_month_deadlines.sort(key=lambda deadline: deadline.date)
        display_deadlines(remaining_month_deadlines)