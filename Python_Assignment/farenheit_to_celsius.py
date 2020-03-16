# convert from fahrenheit to celsius

fahrenheit = float(input('Enter the fahrenheit value to convert :'))


class Farenheit_to_Celsius():
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def convert(self):
        celsius = (self.fahrenheit - 32) * 5.0 / 9.0

        return f'\nValue from temperature {self.fahrenheit} fahrenheit to {celsius} celsius has been converted'


F_to_C = Farenheit_to_Celsius(fahrenheit)

print(F_to_C.convert())
