# convert temperature from fahrenheit to celsius

celsius = float(input('Enter the celsius value to convert :'))


class Celsius_to_Farenheit():
    def __init__(self, celsius):
        self.celsius = celsius

    def convert(self):
        farenheit = (self.celsius * 1.8) + 32

        return f'\nEntered celsius value {self.celsius} is converted into {farenheit} farenheit value'


C_to_F = Celsius_to_Farenheit(celsius)

print(C_to_F.convert())
