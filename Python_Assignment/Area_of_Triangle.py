# Calculate the area of triangle

import sys
import math

a = int(input('Enter the first value of triangle :'))
b = int(input('Enter the second value of triangle :'))
c = int(input('Enter the third value of triangle :'))


class Area_Of_Triangle():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_Area(self):
        value = (a + b + c) / 2
        area = math.sqrt(value * (value - a) * (value - b) * (value - c))
        return area


aot = Area_Of_Triangle(a, b, c)
print(f'\nThe Area of Triangle is {aot.find_Area()}')
