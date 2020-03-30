# Finding Highest common factor and Least common factor
import sys

class Hcf_And_Lcm:
    def __init__(self, num1, num2):
        self.num1 = int(num1)
        self.num2 = int(num2)

    def Check(self):
        r = self.num1 % self.num2
        while r != 0:
            self.num1, self.num2 = self.num2, r
            r = self.num1 % self.num2
        h = self.num2
        l = (self.num1 * self.num2) / h
        print('Entered numbers are {} {} and hcf is {} and lcm is {}\n\n'.format(self.num1, self.num2, h, l))


num1 = int(input('Enter any number you want :'))
num2 = int(input('Enter any number you want :'))
HLCM = Hcf_And_Lcm(num1, num2)
HLCM.Check()
