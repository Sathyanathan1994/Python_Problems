# Fibonacci series

class Fibonacci_Series:

    def __init__(self, limit, f, s):
        self.limit = limit
        self.f = f
        self.s = s

    def Operation(self):
        if self.limit < 0:
            return "invalid input"
        elif self.limit == 1 or self.limit == 2:
            return 1
        else:
            print(self.f, self.s, end=" ")
            for x in range(2, limit):
                next = self.f + self.s
                print(next, end=" ")
                self.f = self.s
                self.s = next


f = 0
s = 1
limit = int(input('Enter the limit you want :'))
Fibo = Fibonacci_Series(limit, f, s)
print(Fibo.Operation())
