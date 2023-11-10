from termcolor import colored

def search_by_name(deadlines_list):
    while True:
        search_name = input("Név (0 kilép): ")
        if search_name == '0':
            return False
        elif search_name == "" or search_name.isspace():
            print(f"{colored('Hibás formátum. Próbáld újra.', 'white', 'on_red')}")
        else:
            search_name = search_name.lower().replace(" ", "")
            found_items = []
            for deadline in deadlines_list:
                if deadline.name.lower().replace(" ", "") == search_name:
                    found_items.append(deadline)
            return found_items
