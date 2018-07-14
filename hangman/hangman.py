# Hangman jogo da forca
import re


class HangMan(object):

    def __init__(self):
        self.secret_word = self.get_word()
        self.guessed_letters = []
        self.missed_letters = []

    def get_word(self):
        return "casa"

    def is_valide(self, letter):
        if not self.match_regex(letter):
            raise ValueError("Este caracter é inválido.")
        elif len(letter) > 1:
            raise ValueError("Mais de um caracter jogado")
        elif (letter in self.guessed_letters) or (letter in self.missed_letters):
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
            return False
        else:
            if (letter in self.secret_word):
                self.guessed_letters.append(letter)
            else:
                self.missed_letters.append(letter)
            return True

    def show_secret_word(self):
        pattern = ""
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                pattern += "_ "
            else:
                pattern += "{} ".format(letter)
        return pattern.strip()

    def won_game(self):
        return "_" not in self.show_secret_word()

    def lost_game(self):
        return len(self.missed_letters) == 6


def main():
    pass


# def if __name__ == '__main__':
#     main()
