import unittest
from hangman.Hangman import Hangman

class TestHangmanGame(unittest.TestCase):
    def test_start_new_game(self):
        hangman = Hangman("word")
        self.assertTrue(type(hangman) is Hangman)
        

    def test_is_game_running(self):
        hangman = Hangman("word")
        self.assertTrue(hangman.is_game_running())

        hangman = Hangman("")
        self.assertFalse(hangman.is_game_running())

    def test_take_guess(self):
        hangman = Hangman("word")
        self.assertTrue(hangman.take_guess("w"))
        self.assertFalse(hangman.take_guess("t"))

    def test_user_has_won(self):
        hangman = Hangman("word")
        self.assertFalse(hangman.user_has_won())

    def test_show_status(self):
        hangman = Hangman("word")
        self.assertTrue(hangman.show_status() == "____")

        hangman.take_guess("w")

        self.assertTrue(hangman.show_status() == "w___")
