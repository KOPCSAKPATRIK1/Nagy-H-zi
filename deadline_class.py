from datetime import datetime

class Deadline:

    def __init__(self, name, date, time, place, desc) -> None:
        self.name = name
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.time = datetime.strptime(time, '%H:%M').time()
        self.place = place
        self.desc = desc 
    