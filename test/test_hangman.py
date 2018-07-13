from unittest import TestCase

from hangman.hangman import HangMan


class TestHangMan(TestCase):

    def setUp(self):
        self.game = HangMan()

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
