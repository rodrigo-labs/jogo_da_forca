# Hangman jogo da forca
import re
import random
import os


board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


class HangMan(object):

    BASE_PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        # self.secret_word = self.get_word()
        self.secret_word = self.get_word()
        self.guessed_letters = []
        self.missed_letters = []

    def get_word(self):
        with open(self.BASE_PATH + "/words.txt", "rt") as file:
                words = file.readlines()

        random_number = random.randint(0, len(words) - 1)
        return words[random_number].strip()
        

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
        except ValueError as e:
            print("Erro: {}".format(e.args[0]))
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

    def end_game(self):
        return self.won_game() or self.lost_game()

    def print_status(self):
        print(board[len(self.missed_letters)])
        print("\nPalavra: " + self.show_secret_word())
        print("\nLetras erradas: ",) 
        for letter in self.missed_letters:
            print(letter)

        print("Letras corretas: ",)
        for letter in self.guessed_letters:
            print(letter)


def main():
    game = HangMan()

    while not game.end_game():
        game.print_status()
        game.guess(input("\nDigite uma letra: "))
        game.print_status()

        if (game.won_game()):
            print("\nParabéns! você ganhou!!!")
        else:
            print("\nGame Over! você perdeu!!!")
            print("A palavra secreta era: " + game.secret_word)


if __name__ == '__main__':
    main()
