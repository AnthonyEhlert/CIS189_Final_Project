"""
Program: Attempt.py
Author: Tony Ehlert
Last date modified: 04/26/2023

The purpose of this program is to define an Attempt class to be used within a Wordle guessing game
The input is required information and code to define the class
The output is print statements to the console to test class
"""
import datetime

from WordleGameEhlert.model.WordleWord import WordleWord


class Attempt():
    """Attempt class"""
    def __init__(self, wordle_word):
        self._wordle_word = wordle_word
        self._date_attempted = datetime.datetime.today().date()
        self._guessed_correct = False
        self._num_of_guesses = 0
        self._wrong_letters = []

    # GETTERS AND SETTERS
    @property
    def wordle_word(self):
        return self._wordle_word

    @wordle_word.setter
    def set_wordle_word(self, wordle_word):
        self._wordle_word = wordle_word

    @property
    def date_attempted(self):
        return self._date_attempted

    @date_attempted.setter
    def set_date_attempted(self, date_attempted):
        self._date_attempted = date_attempted

    @property
    def guessed_correct(self):
        return self._guessed_correct

    @guessed_correct.setter
    def set_guessed_correct(self, guessed_correct):
        self._guessed_correct = guessed_correct

    @property
    def num_of_guesses(self):
        return self._num_of_guesses

    @num_of_guesses.setter
    def set_num_of_guesses(self, num_of_guesses):
        self._num_of_guesses = num_of_guesses

    @property
    def wrong_letters(self):
        return self._wrong_letters

    @wrong_letters.setter
    def set_wrong_letters(self, wrong_letters):
        self._wrong_letters = wrong_letters

    def __str__(self):
        str_string = f"Attempt(Wordle Word: \"{self._wordle_word.word}\""
        str_string += f", Date of Attempt: {self._date_attempted}"
        str_string += f", Guessed Correct: {self._guessed_correct}"
        str_string += f", Number of Guesses: {self._num_of_guesses}"
        str_string += f", Wrong Letters Guessed: {self._wrong_letters}"
        return str_string

    def __repr__(self):
        return "Attempt(" + str(self._wordle_word.__repr__()) + ")"

# Driver/Main
if __name__ == "__main__":

    # create WordleWord object ot pass to Attempt constructor
    test_wordle_word = WordleWord("trust")

    # create attempt object
    test_attempt = Attempt(test_wordle_word)

    # test __str__ and __repr__ methods
    print(test_attempt)
    print(test_attempt.__repr__())

    # garbage collection
    del test_wordle_word
    del test_attempt
