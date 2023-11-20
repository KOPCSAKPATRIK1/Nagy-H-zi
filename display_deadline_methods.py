from deadline_class import Deadline
from termcolor import colored

def display_deadlines(deadlines_list: list[Deadline]):
    max_name_length = max(len(deadline.name) for deadline in deadlines_list)
    max_date_length = max(len(deadline.date) for deadline in deadlines_list)
    max_time_length = max(len(deadline.time) for deadline in deadlines_list)
    max_place_length = max(len(deadline.place) for deadline in deadlines_list)
    sorted_deadlines = sorted(deadlines_list, key=lambda x: x.date)

    for index, deadline in enumerate(sorted_deadlines, start=1):
        print(f"{index}. {deadline.name:<{max_name_length + 5}}{deadline.date:<{max_date_length + 5}}{deadline.time:<{max_time_length + 5}}{deadline.place:<{max_place_length + 5}}{deadline.desc}")

