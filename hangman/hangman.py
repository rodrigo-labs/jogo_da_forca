# Hangman jogo da forca
import re


class HangMan(object):

    def __init__(self):
        self.secret_word = self.get_word()
        self.guesses = []
        self.hits = 0
        self.errors = 0

    def get_word(self):
        return "palavra"

    def is_valide(self, letter):
        if not self.match_regex(letter):
            raise ValueError("Este caracter é inválido.")
        elif len(letter) > 1:
            raise ValueError("Mais de um caracter jogado")
        elif letter in self.guesses:
            raise ValueError("Este caracter já foi jogado")
        letter = letter.lower()
        return letter

    def match_regex(self, letter):
        return re.match("[A-Za-záàâãéèêíïóôõöúçÁÀÂÃÉÈÍÏÓÔÕÖÚÇ]", letter)

    def guess(self, letter):
        try:
            letter = self.is_valide(letter)
        except ValueError as ve:
            print("Erro: {}".format(ve.args[0]))
        else:
            self.guesses.append(letter)
            

        
        


def main():
    pass


# def if __name__ == '__main__':
#     main()
