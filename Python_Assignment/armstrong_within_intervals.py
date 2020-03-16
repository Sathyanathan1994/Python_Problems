# Printing armstrong number within intervals

start = int(input('Enter starting value of number :'))

end = int(input('Enter ending value of a number :'))


class Armstrong_Within_Intervals:

    def __init__(self, start, end):

        self.start = start
        self.end = end

    def check(self):

        for number in range(self.start, self.end):
            digits = 0
            temp = number
            while temp > 0:
                digits += 1
                temp //= 10
            sum1 = 0
            temp = number
            while temp > 0:
                last_digit = temp % 10
                sum1 = sum1 + (last_digit ** digits)
                temp //= 10
            if number == sum1:
                print (number)


AWI = Armstrong_Within_Intervals(start, end)
print('The Armstrong numbers in between ranges are...')
print(AWI.check())