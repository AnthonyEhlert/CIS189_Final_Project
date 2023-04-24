"""
Program: WordleGame
Author: Tony Ehlert
Last date modified: 4/26/2023

The purpose of this program is define a WordleGame object used to store the game information
The input is required information and code to define the class
The output is print statements to the console to test class
"""
import random

from WordleGameEhlert.model.Attempt import Attempt
from WordleGameEhlert.model.WordleWord import WordleWord


class WordleGame():
    """WordleGame Class"""

    def __init__(self, valid_word_set):
        def create_valid_word_dict(valid_word_set):
            """
            Creates a dictionary of WordleWords from words contained in a set of words with the WordleWord objects
            serving as values and an integer as the key

            :param valid_word_set: set of words to be used to create WordleWord objects
            :return: valid_word_dict: dictionary of valid words
            """
            valid_word_dict = {}
            id_num = 1
            for word in valid_word_set:
                wordle_word_object = WordleWord(word)
                valid_word_dict[id_num] = wordle_word_object
                id_num += 1
            return valid_word_dict

        self._valid_word_dict = create_valid_word_dict(valid_word_set)
        self._user_attempt = None
        self._num_of_words_attempted = 0
        self._num_guessed_correct = 0

    def generate_random_attempt(self):
        """
        This method creates a randomly selected Attempt object

        :return: newly created Attempt object
        """
        # use random number to grab object from dictionary
        random_key = random.randint(1, len(self._valid_word_dict))

        # create empty set of numbers/keys to store numbers already used
        used_keys = set()

        # create variable to signify valid random_key
        random_key_valid = False

        while not random_key_valid:
            # select object based on number/key from dictionary and check for attempted
            if self._valid_word_dict[random_key].attempted:
                used_keys.add(random_key)
                random_key = random.randint(1, len(self._valid_word_dict))

                # while new random number/key in used set generate new number
                while random_key in used_keys:
                    random_key = random.randint(1, len(self._valid_word_dict))

            else:
                random_key_valid = True
        ### create Attempt object using selected object from dictionary
        # set WordleWord object._attempted to True
        self._valid_word_dict[random_key].set_attempted = True

        # update words_attempted count
        self._num_of_words_attempted += 1

        # create Attempt object and set it object's user_attempt variable
        self._user_attempt = Attempt(self._valid_word_dict[random_key])

    @property
    def valid_word_dict(self):
        return self._valid_word_dict

    @valid_word_dict.setter
    def set_valid_word_dict(self, valid_word_dict):
        self._valid_word_dict = valid_word_dict

    @property
    def num_of_words_attempted(self):
        return self._num_of_words_attempted

    @num_of_words_attempted.setter
    def set_num_of_words_attempted(self, num_of_words_attempted):
        self._num_of_words_attempted = num_of_words_attempted

    @property
    def num_guessed_correct(self):
        return self._num_guessed_correct

    @num_guessed_correct.setter
    def set_num_guessed_correct(self, num_guessed_correct):
        self._num_guessed_correct = num_guessed_correct

    @property
    def user_attempt(self):
        return self._user_attempt

    @user_attempt.setter
    def set_user_attempt(self, user_attempt):
        self._user_attempt = user_attempt

    def __str__(self):
        str_string = f"WordleGame(Valid Words Dictionary: {self._valid_word_dict}, "
        str_string += f"Number of Words Attempted: {self._num_of_words_attempted}, "
        if self._user_attempt == None:
            str_string += f"User Attempt: None"
        else:
            str_string += f"Current User Attempt Word: {self._user_attempt._wordle_word.word})"
        return str_string

    def __repr__(self):
        repr_string = "WordleGame(" + str(self._valid_word_dict) + ")"
        return repr_string

if __name__ == "__main__":
    # create test word list
    test_word_list = ["START", "WRONG", "RIGHT"]

    # convert list to set
    test_word_set = set(test_word_list)

    # create test_game object
    test_game = WordleGame(test_word_set)

    # print __str__ to ensure user_attempt == None and Number of words attempted == 0
    print(test_game)

    # generate random attempt
    test_game.generate_random_attempt()

    # print test_game __str__ and __repr__ methods
    print(test_game)
    print(test_game.__repr__())

    # garbage collection
    del test_game
    del test_word_set
    del test_word_list
