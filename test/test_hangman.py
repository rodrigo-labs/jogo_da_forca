from unittest import TestCase

from hangman.hangman import HangMan


class TestHangMan(TestCase):

    def setUp(self):
        self.game = HangMan()
        self.game.secret_word = 'casa'

    def test_get_word(self):
        self.assertEqual(self.game.get_word(), "casa")

    def test_is_valide(self):
        self.assertTrue(self.game.is_valide("a"))

    def test_is_valide_uppercase(self):
        self.assertTrue(self.game.is_valide("A"))

    def test_is_valide_two_letter(self):
        with self.assertRaises(Exception):
            self.assertFalse(self.game.is_valide("aa"))

    def test_is_valide_empty_string(self):
        with self.assertRaises(Exception):
            self.assertFalse(self.game.is_valide(""))

    def test_is_valide_space(self):
        with self.assertRaises(Exception):    
            self.assertFalse(self.game.is_valide(" "))

    def test_is_valide_number(self):
        with self.assertRaises(Exception):
            self.assertFalse(self.game.is_valide("5"))

    def test_is_valide_another_character(self):
        with self.assertRaises(Exception):
            self.assertFalse(self.game.is_valide("+"))

    def test_is_valide_with_repeated_character(self):
        with self.assertRaises(Exception):
            self.assertTrue(self.game.is_valide("a"))
            self.assertFalse(self.game.is_valide("a"))

    def test_guess(self):
        self.game.guess("c")
        self.game.guess("q")
        self.assertEqual("c", self.game.guessed_letters[0])
        self.assertEqual("q", self.game.missed_letters[0])

    def test_show_secret_word_no_plays(self):
        self.assertEqual("_ _ _ _", self.game.show_secret_word())

    def test_show_secret_word_with_one_hit(self):
        self.game.guess("a")
        self.game.guess("q")
        self.assertEqual("_ a _ a", self.game.show_secret_word())

    def test_won_game(self):
        self.game.guess("a")
        self.game.guess("c")
        self.assertFalse(self.game.won_game())
        self.game.guess("s")
        self.assertTrue(self.game.won_game())

    def test_lost_game(self):
        self.game.guess("q")
        self.game.guess("w")
        self.game.guess("e")
        self.game.guess("r")
        self.game.guess("t")
        self.game.guess("y")
        self.assertTrue(self.game.lost_game())

    def test_end_game_whit_won_game(self):
        self.game.guess("a")
        self.game.guess("c")
        self.game.guess("q")
        self.game.guess("s")
        self.assertTrue(self.game.end_game())

    def test_end_game_with_lost_game(self):
        self.game.guess("q")
        self.game.guess("w")
        self.game.guess("a")
        self.game.guess("e")
        self.game.guess("r")
        self.game.guess("t")
        self.game.guess("y")
        self.assertTrue(self.game.end_game())

    def teste_print_status(self):
        self.game.print_status()
