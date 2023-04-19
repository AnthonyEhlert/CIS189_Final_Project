"""
Program: WordleWordTestCase.py
Author: Tony Ehlert
Last date modified: 4/21/2023

The purpose of this program is to test the WordleWord class
The input is tests and necessary variables to test the WordleWord class
The output is results of the tests
"""
import unittest

from WordleGameEhlert.model.WordleWord import WordleWord


class WordleWordTestCase(unittest.TestCase):
    def setUp(self):
        self.wordle_word = WordleWord("trust")

    def tearDown(self):
        del self.wordle_word

    def test_object_created_lower_case_attribute(self):
        """
        Tests to ensure object was created correctly with provided lower case attribute and has correct default values
        """
        self.assertEqual(self.wordle_word.word, "TRUST")
        self.assertEqual(self.wordle_word.attempted, False)

    def test_object_created_upper_case_attribute(self):
        """
        Tests to ensure object was created correctly with provided upper case attribute and has correct default values
        """
        wordle_word = WordleWord("TRUST")
        self.assertEqual(wordle_word.word, "TRUST")
        self.assertEqual(wordle_word.attempted, False)

    def test_object_created_mixed_case_attribute(self):
        """
        Tests to ensure object was created correctly with provided mixed case attribute and has correct default values
        """
        wordle_word = WordleWord("TruST")
        self.assertEqual(wordle_word.word, "TRUST")
        self.assertEqual(wordle_word.attempted, False)

    def test_object_not_created_error_word(self):
        """
        Tests to ensure no numbers are in word and that word is correct length
        """
        with self.assertRaises(ValueError):
            num_in_word = WordleWord("The12")
        with self.assertRaises(ValueError):
            too_long_word = WordleWord("Sample")
        with self.assertRaises(ValueError):
            too_short_word = WordleWord("This")


    def test_str(self):
        """
        Tests the overriden __str__ method
        """
        self.assertEqual(self.wordle_word.__str__(), "Wordle Word(Word: \"TRUST\", Attempted: False)")

    def test_repr(self):
        """
        Tests the overriden __repr__ method
        """
        self.assertEqual(self.wordle_word.__repr__(), "WordleWord(\"TRUST\")")

# Driver/Main
if __name__ == "__main__":
    WordleWordTestCase.main()