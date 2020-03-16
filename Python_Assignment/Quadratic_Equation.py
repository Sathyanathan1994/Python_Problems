# Find the quadratic equation
import cmath

a = int(input('Enter the number of a value :'))
b = int(input('Enter the number of b value :'))
c = int(input('Enter the number of c value :'))


class Quadratic_Equation():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.d = (b ** 2) - (4 * a * c)

    def is_quadratic_equation(self):
        val1 = (-b - cmath.sqrt(self.d)) / (2 * a)
        val2 = (-b + cmath.sqrt(self.d)) / (2 * a)

        return f'Value of quadratic equation is {val1} and {val2}'


qde = Quadratic_Equation(a, b, c)

print(f'\nValue of quadratic equation is {qde.is_quadratic_equation()}')
