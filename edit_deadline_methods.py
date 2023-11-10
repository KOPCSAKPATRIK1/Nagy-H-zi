from hatarido_class import Hatarido

def select(deadlines_list: list[Hatarido]):
    while True:
            for index, deadline in enumerate(deadlines_list, start=1):
                print(f"{index}. {deadline.name}; {deadline.date}; {deadline.time}")
            try:
                choose = input("Melyiket szeretnéd módosítani? (0 kilép): ")
                choose = int(choose)

                if 1 <= choose <= len(deadlines_list):
                    selected = deadlines_list[choose-1]
                    print(f"Kiválasztott elem: {selected.name}; {selected.date}; {selected.time}; {selected.place}; {selected.desc}")
                elif choose == 0:
                    print("Kilépés...")
                    return False
                else:
                    print("Érvénytelen választás. Kérlek válassz újra.")
            except ValueError:
                print("Érvénytelen bemenet. Kérlek számot adj meg.")
            except IndexError:
                print("Nincs ilyen index az adott listában. Kérlek válassz újra.")
            except Exception as e:
                print(f"Hiba történt: {e}") 