# convert decimal to binary, octal and hexadecimal in python


class Dec_To_BOH:
    def __init__(self, num):
        self.num = num

    def Dec_To_Binary(self):
        decimal = int(self.num)

        print(decimal, "in binary : ", bin(decimal))

    def Dec_To_Octal(self):
        decimal = int(self.num)

        print(decimal, "in Octal : ", oct(decimal))

    def Dec_To_Hex(self):
        decimal = int(self.num)

        print(decimal, "In Hexadecimal : ", hex(decimal))


num = int(input('Enter any number :'))
BOH = Dec_To_BOH(num)
BOH.Dec_To_Binary()
BOH.Dec_To_Octal()
BOH.Dec_To_Hex()
