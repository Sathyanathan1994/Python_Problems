# check whether its leap year or not

year = int(input('Enter the year you want to find whether leap or not :'))


class Leap_Year:
    def __init__(self, year):
        self.year = year

    def check(self):

        if (self.year % 4) == 0:

            if (self.year % 100) == 0:

                if (self.year % 400) == 0:
                    print(f'Year you mentioned {self.year} is leap year')

                else:
                    print(f'Year you mentioned {self.year} is not a leap year')

            else:
                print(f'Year you mentioned {self.year} is leap year')

        else:
            print(f'Year you mentioned {self.year} is not a leap year')


LPY = Leap_Year(year)

print('\n', LPY.check())
