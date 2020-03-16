# prime number in given interval

start = int(input('Enter the starting point of value :'))

end = int(input('Enter the ending point of value :'))


class Prime_Number:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def finding_prime_number(self):
        for num in range(self.start, self.end + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(f'Given interval of Prime number is {num}')


PN = Prime_Number(start, end)

print(PN.finding_prime_number())
