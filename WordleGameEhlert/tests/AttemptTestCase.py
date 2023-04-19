"""
Program: AttemptTestCase.py
Author: Tony Ehlert
Last date modified: 4/21/2023

The purpose of this program is to test the Attempt class
The input is tests and necessary variables to test the Attempt class
The output is results of the tests
"""
import datetime
import unittest

from WordleGameEhlert.model.Attempt import Attempt
from WordleGameEhlert.model.WordleWord import WordleWord


class AttemptTestCase(unittest.TestCase):
    def setUp(self):
        self.attempt = Attempt(WordleWord("TRUST"))

    def tearDown(self):
        del self.attempt

    def test_object_created(self):
        """
        Tests to ensure object was created correctly with provided attribute and has correct default values
        """
        self.assertEqual(self.attempt.wordle_word.word, "TRUST")
        self.assertEqual(self.attempt.date_attempted, datetime.date.today())
        self.assertEqual(self.attempt.guessed_correct, False)
        self.assertEqual(self.attempt.num_of_guesses, 0)

    def test_str(self):
        """
        Tests the overriden __str__ method
        """
        expected_string = "Attempt(Wordle Word: \"TRUST\", Date of Attempt: " + str(
            datetime.date.today()) + ", Guessed Correct: False, Number of Guesses: 0"
        self.assertEqual(self.attempt.__str__(), expected_string)

    def test_repr(self):
        """
        Tests the overriden __repr__ method
        """
        self.assertEqual(self.attempt.__repr__(), "Attempt(WordleWord(\"TRUST\"))")

# Driver/Main
if __name__ == "__main__":
    AttemptTestCase.main()