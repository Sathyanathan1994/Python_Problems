# Kilometer to mile conversion in python

km = float(input('Enter the kilometer range :'))


class Km_To_Mile():

    def __init__(self, km):
        self.km = km

        # conversion factor
        self.cf = 0.621371

    def convert(self):
        mile = self.km * self.cf

        return f'The kilometer range {self.km} has been converted into {mile} miles valiue'


k_to_m = Km_To_Mile(km)

print(f'\nThe value is {k_to_m.convert()}')
