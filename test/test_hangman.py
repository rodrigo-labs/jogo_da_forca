from unittest import TestCase

from hangman.hangman import HangMan


class TestHangMan(TestCase):

    def setUp(self):
        self.game = HangMan()

    def test_get_word(self):
        self.assertEqual(self.game.get_word(), "palavra")

    def test_guess_correct(self):
        self.assertTrue(self.game.guess("a"))

    def test_guess_error(self):
        self.assertFalse(self.game.guess("z"))

    def test_guess_uppercase(self):
        self.assertTrue(self.game.guess("A"))

    def test_guess_two_letter(self):
        with self.assertRaises(Exception):
            self.assertFalse(self.game.guess("aa"))

    def test_guess_empty_string(self):
        with self.assertRaises(Exception):
            self.assertFalse(self.game.guess(""))

    def test_guess_space(self):
        with self.assertRaises(Exception):    
            self.assertFalse(self.game.guess(" "))

    def test_guess_number(self):
        with self.assertRaises(Exception):
            self.assertFalse(self.game.guess("5"))

    def test_guess_another_character(self):
        with self.assertRaises(Exception):
            self.assertFalse(self.game.guess("+"))
