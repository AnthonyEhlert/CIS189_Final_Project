"""
Program: test_driver.py
Author: Tony Ehlert
Last date modified: 4/21/2023

The purpose of this program is note and test steps needed to completed CIS189_Final_Project
The input is various data, code, and comments to test different functions and processes
The output is print statements to the console
"""

import random
import array as arr

from WordleGameEhlert.model.Attempt import Attempt
from WordleGameEhlert.model.WordleWord import WordleWord

# # create list of words as strings
# word_list = ["trust", "wrong", "right", "happy", "above", "again", "strip", "coded", "glass", "month", "Month"]
# #word_list += ["radio", "paper", "stand", "niece", "named", "Video"]
#
# # create new list of words using word_list words and converting to upper case as first step to ensure no duplicates
# upper_case_word_list = []
# for word in word_list:
#     upper_case_word_list.append(word.upper())
#
# # convert list to set to ensure no duplicates.
# word_set = set(upper_case_word_list)
# #print(word_set)
# #print(len(word_set))
#
# ### for each word in list, create WordleWord object and add to dictionary(key = int, value = WordleWord object)
# #create empty dictionary to store WordleWord objects
# word_dict = {}
#
# # create id counter variable to use as key in dictionary
# id_num = 1
#
# # create loop to iterate through list of strings
# for word in word_set:
#     wordle_word_object = WordleWord(word)
#     word_dict[id_num] = wordle_word_object
#     id_num += 1
# #print(word_dict)

###create while loop to iterate through dictionary objects until either all words have been attempted or sentinel value
# create sentinel value (only used for testing)
game_sentinel_value = "-1"

# create user_input variable for comparison against sentinel_value
user_input = "0"

# create words_attempted variable for use in controlling while loop
words_attempted = 0

# assign word_dict length to variable to use for while loop and random number limit
word_dict_length = len(word_dict)

while words_attempted < word_dict_length and user_input != game_sentinel_value:
    # use random number to grab object from dictionary
    random_key = random.randint(1, word_dict_length)

    # create empty set of numbers/keys to store numbers already used
    used_keys = set()

    # create variable to signify valid random_key
    random_key_valid = False

    while not random_key_valid:
        # select object based on number/key from dictionary and check for attempted
        if word_dict[random_key].attempted:
            used_keys.add(random_key)
            random_key = random.randint(1, word_dict_length)

            # while new random number/key in used set generate new number
            while random_key in used_keys:
                random_key = random.randint(1, word_dict_length)

        else:
            random_key_valid = True


    ### create Attempt object using selected object from dictionary
    # set WordleWord object._attempted to True
    word_dict[random_key].set_attempted = True

    # create Attempt object
    user_attempt = Attempt(word_dict[random_key])

    # extract word from WordleWord object and convert to array
    char_list = list(user_attempt.wordle_word.word)
    print(char_list)
    word_array = arr.array(char_list)
    print(word_array)
    user_input = input("Please enter your guess: ")


