# check the factorial of a given number within the interval


class Factorial:
    def __init__(self, num):
        self.number = number
        self.fact = 1

    def operation(self):
        if self.number == 0 or self.number == 1:
            return 1
        else:
            for i in range(1, self.number + 1):
                self.fact = self.fact * i
            return f'\nEntered factorial value is {self.fact}'


number = int(input('Enter the number you want :'))
F = Factorial(number)
print(F.operation())
