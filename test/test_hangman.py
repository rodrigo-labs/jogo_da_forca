from unittest import TestCase

from hangman.hangman import HangMan


class TestHangMan(TestCase):

    def setUp(self):
        self.game = HangMan()

    def test_get_word(self):
        self.assertEqual(self.game.get_word(), "palavra")
