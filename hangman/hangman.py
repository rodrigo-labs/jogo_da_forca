# Hangman jogo da forca
import re


class HangMan(object):

    def __init__(self):
        self.secret_word = self.get_word()

    def get_word(self):
        return "palavra"

    def guess(self, letter):
        if not self.match_regex(letter):
            raise ValueError("Caracter inválido.")
        elif len(letter) > 1:
            raise ValueError("Mais de um caracter")
        letter = letter.lower()
        return letter in self.secret_word

    def match_regex(self, letter):
        return re.match("[A-Za-záàâãéèêíïóôõöúçÁÀÂÃÉÈÍÏÓÔÕÖÚÇ]", letter)


def main():
    pass


# def if __name__ == '__main__':
#     main()
