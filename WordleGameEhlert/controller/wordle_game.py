"""
Program: wordle_game.py
Author: Tony Ehlert
Last date modified: 4/26/2023

The purpose of this program is to contain methods that are used to run a Wordle guessing game and perform various tests
of those methods

The input is required information and code to define the methods needed
The output is print statements to the console testing the methods
"""
import random

from WordleGameEhlert.model.Attempt import Attempt
from WordleGameEhlert.model.WordleWord import WordleWord


def start_game():
    """
    This method is called to start the wordle game. It calls other methods to run the wordle game

    :return:
    """
    # create valid word set
    valid_word_set = read_word_list_file()

    # create dictionary of WordleWord objects from words in set
    valid_word_dict = {}
    id_num = 1
    for word in valid_word_set:
        wordle_word_object = WordleWord(word)
        valid_word_dict[id_num] = wordle_word_object
        id_num += 1

    # create sentinel value (only used for testing)
    game_sentinel_value = "-1"

    # create user_guess variable for comparison against sentinel_value
    user_guess = "0"

    # create words_attempted variable for use in controlling while loop
    words_attempted = 0

    # assign word_dict length to variable to use for while loop and random number limit
    word_dict_length = len(valid_word_dict)

    while words_attempted < word_dict_length and user_guess != game_sentinel_value:
        # use random number to grab object from dictionary
        random_key = random.randint(1, word_dict_length)

        # create empty set of numbers/keys to store numbers already used
        used_keys = set()

        # create variable to signify valid random_key
        random_key_valid = False

        while not random_key_valid:
            # select object based on number/key from dictionary and check for attempted
            if valid_word_dict[random_key].attempted:
                used_keys.add(random_key)
                random_key = random.randint(1, word_dict_length)

                # while new random number/key in used set generate new number
                while random_key in used_keys:
                    random_key = random.randint(1, word_dict_length)

            else:
                random_key_valid = True

        ### create Attempt object using selected object from dictionary
        # set WordleWord object._attempted to True
        valid_word_dict[random_key].set_attempted = True

        # update words_attempted count
        words_attempted += 1

        # create Attempt object
        user_attempt = Attempt(valid_word_dict[random_key])

        # extract word from WordleWord object and convert to list
        char_list = list(user_attempt.wordle_word.word)
        print(char_list)

        # create num_of_guesses variable to keep track of guess count
        num_of_guesses = 1

        # create correct_guess boolean variable for while loop
        correct_guess = False

        # create wrong_letters list outside of loop to keep track of wrongs letters used
        wrong_letters = []

        # while loop to check for correct guess or up to five guesses
        while num_of_guesses <= 5 and correct_guess == False:

            # print guess number
            print(f"Word #{words_attempted}, Guess #{num_of_guesses}")

            # get user guess
            user_guess = get_user_guess(valid_word_set)

            # convert user_guess to list
            user_guess_as_list = list(user_guess)
            # print(user_guess)

            # create lists for correct_letters and misplaced_letters
            correct_letters = []
            misplaced_letters = []

            if user_guess_as_list == char_list:
                print("Correct")
                correct_guess = True
                user_attempt.set_num_of_guesses = num_of_guesses
                user_attempt.set_guessed_correct = True
            elif user_guess == game_sentinel_value:
                print("Game Ended")
                break
            elif num_of_guesses <= 4:
                char_count = 0
                for char in user_guess_as_list:
                    if char_list[char_count] == user_guess_as_list[char_count]:
                        correct_letters.append(char)
                        # remove char from misplaced letters list if present
                        if char in misplaced_letters:
                            misplaced_letters.remove(char)
                        char_count += 1
                    elif char in char_list and char not in correct_letters:
                        correct_letters.append("_")
                        misplaced_letters.append(char)
                        char_count += 1
                    else:
                        correct_letters.append("_")
                        wrong_letters.append(char)
                        char_count += 1
                # convert letter lists to sets to remove duplicates
                print("Incorrect")
                print(f"Correct Letters: {correct_letters}")
                print(f"Misplaced Letters: {set(misplaced_letters)}")
                print(f"Wrong Letters: {set(wrong_letters)}")

                num_of_guesses += 1
            else:
                print(f"Incorrect, Correct word was{char_list}")
                num_of_guesses += 1
                user_attempt.set_num_of_guesses = num_of_guesses


def read_word_list_file():
    """
    This method is called to read a .txt file containing valid wordle words and put them into a list

    :return: set of valid wordle words
    """
    with open('wordle_word_list.txt') as file:
        # create empty list
        word_list = []

        # read each word from file and place in list
        for line in file:
            line = line.strip()
            try:
                word_list.append(line.upper())
            except:
                print("Failed to convert to string")
    # return list as set
    return set(word_list)


def get_user_guess(valid_word_set):
    """
    This method is used to prompt the user for the next word they would like to guess

    :param valid_word_set: set of valid words to be used for user input validation
    :return: word that is to be used as user's guess
    """

    def valid_guess(user_guess, valid_word_set):
        """
        This method is used to check if the user's guess is valid

        :param user_guess: word to be checked if valid
        :param valid_word_set: set of valid words
        :return: boolean if user guess is valid
        """
        user_guess = user_guess.upper()
        # check if guess is contained in valid_word_dict
        if user_guess in valid_word_set or user_guess == "-1":
            return True
        else:
            return False

    # prompt user for input
    user_guess = input("Please enter your guess: ")

    while not valid_guess(user_guess, valid_word_set):
        user_guess = input("Not a valid word! Please enter your guess: ")

    return user_guess.upper()


if __name__ == "__main__":
    # # create valid word set
    # valid_word_set = read_word_list_file()

    # start game
    start_game()
