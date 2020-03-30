# Printing calendar in python
import calendar


class Calendar:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def Call(self):
        print(calendar.month(self.year, self.month))


year = int(input('Enter the year you want :'))
month = int(input('Enter the month you want :'))
C = Calendar(year, month)