"""
Program: WordleGameTestCase.py
Author: Tony Ehlert
Last date modified: 4/24/2023

The purpose of this program is to test the WordleGame class
The input is tests and necessary variables to test the WordleGame class
The output is results of the tests
"""
import unittest

from WordleGameEhlert.model.WordleGame import WordleGame
from WordleGameEhlert.model.WordleWord import WordleWord


class WordleGameTestCase(unittest.TestCase):
    def setUp(self):
        self.test_game = WordleGame({"WRONG"})

    def tearDown(self):
        del self.test_game

    def test_object_created(self):
        """
        Tests to ensure object was created correctly with provided attribute and has correct default values
        """
        self.assertEqual(self.test_game.valid_word_dict[1].word, "WRONG")
        self.assertEqual(self.test_game.num_of_words_attempted, 0)
        self.assertEqual(self.test_game.user_attempt, None)
        self.assertEqual(self.test_game.num_guessed_correct, 0)

    def test_generate_random_attempt(self):
        """
        This test is to ensure the num_of_words_attempted variable is increased by one and that an attempt
        is generated and assigned to the user_attempt variable after the generate_random_attempt method is called
        """
        self.test_game.generate_random_attempt()
        self.assertEqual(self.test_game.num_of_words_attempted, 1)
        self.assertEqual(self.test_game.user_attempt.wordle_word.word, "WRONG")

    def test_str(self):
        """
        Tests the overriden __str__ method
        """
        expected_str = "WordleGame(Valid Words Dictionary: {1: WordleWord(\"WRONG\")}, Number of Words Attempted: 0, User Attempt: None"
        self.assertEqual(self.test_game.__str__(), expected_str)

    def test_repr(self):
        """
        Tests the overriden __repr__ method
        """
        self.assertEqual(self.test_game.__repr__(), "WordleGame({1: WordleWord(\"WRONG\")})")

if __name__ == "__main__":
    WordleGameTestCase.main()