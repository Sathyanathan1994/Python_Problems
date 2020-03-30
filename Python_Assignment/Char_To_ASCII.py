# Convert Character to ASCII Value


class Char_Ascii:
    def __init__(self, word):
        self.word = word

    def check(self):
        print(f"ASCII Value of word {self.word} is", ord(self.word))


word = input('Enter any character you want :')
if len(word) == 1:
    print('Entered character value is accepted!')
else:
    print('Character does not accepted!\nPlease specify single character value!')


CASC = Char_Ascii(word)
CASC.check()
