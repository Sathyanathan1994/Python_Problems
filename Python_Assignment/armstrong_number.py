# Armstrong number within given intervals

number = int(input('Enter the number :'))

class Armstrong:

    def __init__(self, number):

        self.number = number

    def check(self):

        temp = self.number
        res = 0

        while temp != 0:
            rem = temp % 10

            res += rem ** 3

            temp //= 10

        if self.number == res:
            return f'{self.number} is Armstrong'
        else:
            return f'{self.number} is not an armstrong number'


Arm = Armstrong(number)

print(Arm.check())
