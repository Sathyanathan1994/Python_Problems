# Decimal to binary in python


class Decimal_To_Binary:
    def __init__(self, dec_value):
        self.dec_value = dec_value

    def Operation(self):
        if self.dec_value > 1:
            Decimal_To_Binary.Operation(self.dec_value // 2)
        print(self.dec_value % 2)


dec_value = int(input('Enter the value to convert into binary :'))
DTB = Decimal_To_Binary(dec_value)
print(DTB.Operation())
