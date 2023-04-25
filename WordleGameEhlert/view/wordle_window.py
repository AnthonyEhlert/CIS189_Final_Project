"""
Program: wordle_window.py
Author: Tony Ehlert
Last date modified: 4/24/2023

The purpose of this program is run a GUI that implements/runs a Wordle guessing game
The input is required code and methods to create and run the GUI
The output is a functional Wordle game GUI
"""
#imports
import tkinter as tk
from tkinter import SUNKEN, CENTER, NORMAL, DISABLED, END, NONE, FLAT, font

from WordleGameEhlert.constants import MAX_GUESSES
from WordleGameEhlert.model.WordleGame import WordleGame


'''
GLOBAL VARIABLE CODE BELOW HERE
'''
# create global valid_word_set
valid_word_set = {}
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

valid_word_set = set(word_list)
#print(valid_word_set)

# create global WordleGame object
wordle_game = WordleGame(valid_word_set)

# generate first attempt in wordle_game
wordle_game.generate_random_attempt()

# create empty letter_label dictionary (key = letter, value = tkinter label)
letter_lbl_dict = {}

# create empty list to hold lists of row letter guesses
list_letter_row_lbls = []

'''
GLOBAL VARIABLE CODE BELOW HERE
'''

'''
FUNCTIONS BELOW HERE
'''
def start_game():
    """
    This method enables the entry_guess field and submit_btn and also populates the lbl_current_word_num label text
    :return:
    """
    submit_btn.config(state=NORMAL)
    entry_guess.config(state=NORMAL)
    lbl_current_word_num.config(text= wordle_game.num_of_words_attempted)
    lbl_num_guessed_correct.config(text= wordle_game.num_guessed_correct)
    start_game_btn.config(state=DISABLED)
    next_word_btn.config(state=NORMAL)

def create_row_letter_labels():
    """
    This method contains three inner functions that each create a row of letter labels within the main_window
    :return:
    """
    def create_row_2_letters():
        """
        this method creates the letter labels for row 2 and adds them to the letter_lbl_dict
        :return:
        """
        # create letter labels for row 2 and add to dictionary
        lbl_letter_q = tk.Label(main_window, text='Q', justify='center')
        lbl_letter_q.grid(row=2, column=2, rowspan=1, columnspan=1)
        letter_lbl_dict["Q"]= lbl_letter_q

        lbl_letter_w = tk.Label(main_window, text='W', justify='center')
        lbl_letter_w.grid(row=2, column=3, rowspan=1, columnspan=1)
        letter_lbl_dict["W"] = lbl_letter_w

        lbl_letter_e = tk.Label(main_window, text='E', justify='center')
        lbl_letter_e.grid(row=2, column=4, rowspan=1, columnspan=1)
        letter_lbl_dict["E"] = lbl_letter_e

        lbl_letter_r = tk.Label(main_window, text='R', justify='center')
        lbl_letter_r.grid(row=2, column=5, rowspan=1, columnspan=1)
        letter_lbl_dict["R"] = lbl_letter_r

        lbl_letter_t = tk.Label(main_window, text='T', justify='center')
        lbl_letter_t.grid(row=2, column=6, rowspan=1, columnspan=1)
        letter_lbl_dict["T"] = lbl_letter_t

        lbl_letter_y = tk.Label(main_window, text='Y', justify='center')
        lbl_letter_y.grid(row=2, column=7, rowspan=1, columnspan=1)
        letter_lbl_dict["Y"] = lbl_letter_y

        lbl_letter_u = tk.Label(main_window, text='U', justify='center')
        lbl_letter_u.grid(row=2, column=8, rowspan=1, columnspan=1)
        letter_lbl_dict["U"] = lbl_letter_u

        lbl_letter_i = tk.Label(main_window, text='I', justify='center')
        lbl_letter_i.grid(row=2, column=9, rowspan=1, columnspan=1)
        letter_lbl_dict["I"] = lbl_letter_i

        lbl_letter_o = tk.Label(main_window, text='O', justify='center')
        lbl_letter_o.grid(row=2, column=10, rowspan=1, columnspan=1)
        letter_lbl_dict["O"] = lbl_letter_o

        lbl_letter_p = tk.Label(main_window, text='P', justify='center')
        lbl_letter_p.grid(row=2, column=11, rowspan=1, columnspan=1)
        letter_lbl_dict["P"] = lbl_letter_p

    def create_row_3_letters():
        """
        this method creates the letter labels for row 3 and adds them to the letter_lbl_dict
        :return:
        """
        # create letter labels for row 3 and add to dictionary
        lbl_letter_a = tk.Label(main_window, text='A', justify='center')
        lbl_letter_a.grid(row=3, column=2, rowspan=1, columnspan=1)
        letter_lbl_dict["A"] = lbl_letter_a

        lbl_letter_s = tk.Label(main_window, text='S', justify='center')
        lbl_letter_s.grid(row=3, column=3, rowspan=1, columnspan=1)
        letter_lbl_dict["S"] = lbl_letter_s

        lbl_letter_d = tk.Label(main_window, text='D', justify='center')
        lbl_letter_d.grid(row=3, column=4, rowspan=1, columnspan=1)
        letter_lbl_dict["D"] = lbl_letter_d

        lbl_letter_f = tk.Label(main_window, text='F', justify='center')
        lbl_letter_f.grid(row=3, column=5, rowspan=1, columnspan=1)
        letter_lbl_dict["F"] = lbl_letter_f

        lbl_letter_g = tk.Label(main_window, text='G', justify='center')
        lbl_letter_g.grid(row=3, column=6, rowspan=1, columnspan=1)
        letter_lbl_dict["G"] = lbl_letter_g

        lbl_letter_h = tk.Label(main_window, text='H', justify='center')
        lbl_letter_h.grid(row=3, column=7, rowspan=1, columnspan=1)
        letter_lbl_dict["H"] = lbl_letter_h

        lbl_letter_j = tk.Label(main_window, text='J', justify='center')
        lbl_letter_j.grid(row=3, column=8, rowspan=1, columnspan=1)
        letter_lbl_dict["J"] = lbl_letter_j

        lbl_letter_k = tk.Label(main_window, text='K', justify='center')
        lbl_letter_k.grid(row=3, column=9, rowspan=1, columnspan=1)
        letter_lbl_dict["K"] = lbl_letter_k

        lbl_letter_l = tk.Label(main_window, text='L', justify='center')
        lbl_letter_l.grid(row=3, column=10, rowspan=1, columnspan=1)
        letter_lbl_dict["L"] = lbl_letter_l

    def create_row_4_letters():
        """
        this method creates the letter labels for row 4 and adds them to the letter_lbl_dict
        :return:
        """

        # create letter labels for row 4
        lbl_letter_z = tk.Label(main_window, text='Z', justify='center')
        lbl_letter_z.grid(row=4, column=2, rowspan=1, columnspan=1)
        letter_lbl_dict["Z"] = lbl_letter_z

        lbl_letter_x = tk.Label(main_window, text='X', justify='center')
        lbl_letter_x.grid(row=4, column=3, rowspan=1, columnspan=1)
        letter_lbl_dict["X"] = lbl_letter_x

        lbl_letter_c = tk.Label(main_window, text='C', justify='center')
        lbl_letter_c.grid(row=4, column=4, rowspan=1, columnspan=1)
        letter_lbl_dict["C"] = lbl_letter_c

        lbl_letter_v = tk.Label(main_window, text='V', justify='center')
        lbl_letter_v.grid(row=4, column=5, rowspan=1, columnspan=1)
        letter_lbl_dict["V"] = lbl_letter_v

        lbl_letter_b = tk.Label(main_window, text='B', justify='center')
        lbl_letter_b.grid(row=4, column=6, rowspan=1, columnspan=1)
        letter_lbl_dict["B"] = lbl_letter_b

        lbl_letter_n = tk.Label(main_window, text='N', justify='center')
        lbl_letter_n.grid(row=4, column=7, rowspan=1, columnspan=1)
        letter_lbl_dict["N"] = lbl_letter_n

        lbl_letter_m = tk.Label(main_window, text='M', justify='center')
        lbl_letter_m.grid(row=4, column=8, rowspan=1, columnspan=1)
        letter_lbl_dict["M"] = lbl_letter_m

    create_row_2_letters()
    create_row_3_letters()
    create_row_4_letters()

def create_guess_labels():
    """
    This method contains inner functions that create the individual letter labels for each guess and adds them
    to a list and then the list to the list_letter_row_lbls
    :return:
    """

    def create_guess1_labels():
        """
        This method creates the necessary labels for guess 1
        :return:
        """
        # create Guess 1 label for row 6, column 1
        lbl_guess_1 = tk.Label(main_window, text="Guess 1", justify="right")
        lbl_guess_1.grid(row=6, column=1, rowspan=1, columnspan=1)

        # create Guess 1 letter labels and lbl_list for row 6
        guess1_lbl_list = []

        lbl_g1_letter_1 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g1_letter_1.grid(row=6, column=2, rowspan=1, columnspan=2)
        guess1_lbl_list.append(lbl_g1_letter_1)

        lbl_g1_letter_2 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g1_letter_2.grid(row=6, column=4, rowspan=1, columnspan=2)
        guess1_lbl_list.append(lbl_g1_letter_2)

        lbl_g1_letter_3 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g1_letter_3.grid(row=6, column=6, rowspan=1, columnspan=2)
        guess1_lbl_list.append(lbl_g1_letter_3)

        lbl_g1_letter_4 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g1_letter_4.grid(row=6, column=8, rowspan=1, columnspan=2)
        guess1_lbl_list.append(lbl_g1_letter_4)

        lbl_g1_letter_5 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g1_letter_5.grid(row=6, column=10, rowspan=1, columnspan=2)
        guess1_lbl_list.append(lbl_g1_letter_5)

        # add guess1_lbl_list to list_letter_row_lbls (guess1)
        list_letter_row_lbls.append(guess1_lbl_list)

    def create_guess2_labels():
        """
        This method creates the necessary labels for guess 2
        :return:
        """
        # create Guess 2 label for row 8, column 1
        lbl_guess_2 = tk.Label(main_window, text="Guess 2", justify="right")
        lbl_guess_2.grid(row=8, column=1, rowspan=1, columnspan=1)

        # create Guess 2 letter labels and lbl_list for row 8
        guess2_lbl_list = []

        lbl_g2_letter_1 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g2_letter_1.grid(row=8, column=2, rowspan=1, columnspan=2)
        guess2_lbl_list.append(lbl_g2_letter_1)

        lbl_g2_letter_2 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g2_letter_2.grid(row=8, column=4, rowspan=1, columnspan=2)
        guess2_lbl_list.append(lbl_g2_letter_2)

        lbl_g2_letter_3 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g2_letter_3.grid(row=8, column=6, rowspan=1, columnspan=2)
        guess2_lbl_list.append(lbl_g2_letter_3)

        lbl_g2_letter_4 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g2_letter_4.grid(row=8, column=8, rowspan=1, columnspan=2)
        guess2_lbl_list.append(lbl_g2_letter_4)

        lbl_g2_letter_5 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g2_letter_5.grid(row=8, column=10, rowspan=1, columnspan=2)
        guess2_lbl_list.append(lbl_g2_letter_5)

        # add guess2_lbl_list to list_letter_row_lbls (guess2)
        list_letter_row_lbls.append(guess2_lbl_list)

    def create_guess3_labels():
        """
        This method creates the necessary labels for guess 3
        :return:
        """
        # create Guess 3 label for row 10, column 1
        lbl_guess_3 = tk.Label(main_window, text="Guess 3", justify="right")
        lbl_guess_3.grid(row=10, column=1, rowspan=1, columnspan=1)

        # create Guess 3 letter labels and lbl_list for row 10
        guess3_lbl_list = []

        lbl_g3_letter_1 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g3_letter_1.grid(row=10, column=2, rowspan=1, columnspan=2)
        guess3_lbl_list.append(lbl_g3_letter_1)

        lbl_g3_letter_2 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g3_letter_2.grid(row=10, column=4, rowspan=1, columnspan=2)
        guess3_lbl_list.append(lbl_g3_letter_2)

        lbl_g3_letter_3 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g3_letter_3.grid(row=10, column=6, rowspan=1, columnspan=2)
        guess3_lbl_list.append(lbl_g3_letter_3)

        lbl_g3_letter_4 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g3_letter_4.grid(row=10, column=8, rowspan=1, columnspan=2)
        guess3_lbl_list.append(lbl_g3_letter_4)

        lbl_g3_letter_5 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g3_letter_5.grid(row=10, column=10, rowspan=1, columnspan=2)
        guess3_lbl_list.append(lbl_g3_letter_5)

        # add guess3_lbl_list to list_letter_row_lbls (guess3)
        list_letter_row_lbls.append(guess3_lbl_list)

    def create_guess4_labels():
        """
        This method creates the necessary labels for guess 4
        :return:
        """
        # create Guess 4 label for row 12, column 1
        lbl_guess_4 = tk.Label(main_window, text="Guess 4", justify="right")
        lbl_guess_4.grid(row=12, column=1, rowspan=1, columnspan=1)

        # create Guess 4 letter labels and lbl_list for row 12
        guess4_lbl_list = []

        lbl_g4_letter_1 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g4_letter_1.grid(row=12, column=2, rowspan=1, columnspan=2)
        guess4_lbl_list.append(lbl_g4_letter_1)

        lbl_g4_letter_2 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g4_letter_2.grid(row=12, column=4, rowspan=1, columnspan=2)
        guess4_lbl_list.append(lbl_g4_letter_2)

        lbl_g4_letter_3 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g4_letter_3.grid(row=12, column=6, rowspan=1, columnspan=2)
        guess4_lbl_list.append(lbl_g4_letter_3)

        lbl_g4_letter_4 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g4_letter_4.grid(row=12, column=8, rowspan=1, columnspan=2)
        guess4_lbl_list.append(lbl_g4_letter_4)

        lbl_g4_letter_5 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g4_letter_5.grid(row=12, column=10, rowspan=1, columnspan=2)
        guess4_lbl_list.append(lbl_g4_letter_5)

        # add row12_lbl_list to list_letter_row_lbls (guess4)
        list_letter_row_lbls.append(guess4_lbl_list)

    def create_guess5_labels():
        """
        This method creates the necessary labels for guess 5
        :return:
        """
        # create Guess 5 label for row 14, column 1
        lbl_guess_5 = tk.Label(main_window, text="Guess 5", justify="right")
        lbl_guess_5.grid(row=14, column=1, rowspan=1, columnspan=1)

        # create Guess 5 letter labels and lbl_list for row 14
        guess5_lbl_list = []

        lbl_g5_letter_1 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g5_letter_1.grid(row=14, column=2, rowspan=1, columnspan=2)
        guess5_lbl_list.append(lbl_g5_letter_1)

        lbl_g5_letter_2 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g5_letter_2.grid(row=14, column=4, rowspan=1, columnspan=2)
        guess5_lbl_list.append(lbl_g5_letter_2)

        lbl_g5_letter_3 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g5_letter_3.grid(row=14, column=6, rowspan=1, columnspan=2)
        guess5_lbl_list.append(lbl_g5_letter_3)

        lbl_g5_letter_4 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g5_letter_4.grid(row=14, column=8, rowspan=1, columnspan=2)
        guess5_lbl_list.append(lbl_g5_letter_4)

        lbl_g5_letter_5 = tk.Label(main_window, text="_", relief=SUNKEN, justify="center")
        lbl_g5_letter_5.grid(row=14, column=10, rowspan=1, columnspan=2)
        guess5_lbl_list.append(lbl_g5_letter_5)

        # add row14_lbl_list to list_letter_row_lbls (guess5)
        list_letter_row_lbls.append(guess5_lbl_list)

    # destroy previous labels if present
    if list_letter_row_lbls is not None:
        for list in list_letter_row_lbls:
            for label in list:
                label.destroy()

    create_guess1_labels()
    create_guess2_labels()
    create_guess3_labels()
    create_guess4_labels()
    create_guess5_labels()

def set_col_width(col_limit, col_width):
    """
    This method creates empty labels for each column with the provided col_width argument to set the width
    for all columns across grid

    :param col_limit: total number of columns in grid
    :param col_width: width of empty labels used to set column widths
    :return:
    """
    for x in range(1, col_limit):
        lbl_empty_col = tk.Label(main_window, text='', width=col_width)
        lbl_empty_col.grid(row=0, column=x)

def submit_guess():
    """
    This method sets the user_guess variable to the contents of the entry_guess text area and first verifies that it
    is a valid entry and then checks if it matches the current word.  It also updates the main_window labels
    :return:
    """

    # assign user_guess to contents of entry_guess
    user_guess = entry_guess.get()

    # clear entry_guess
    entry_guess.delete(0, END)
    print(user_guess)

    # check submission to ensure it is valid
    if user_guess.upper() not in valid_word_set:
        lbl_submitted_guess.config(text="Invalid Entry", fg= "red")
        return

    # verification that word has not been correctly guessed and that num_of_guesses has not exceeded MAN_GUESSES
    if (wordle_game.user_attempt.guessed_correct == False) and (wordle_game.user_attempt.num_of_guesses <= MAX_GUESSES):
        # increment the number of guesses by one
        wordle_game.user_attempt.set_num_of_guesses += 1

        #print(wordle_game.user_attempt.wrong_letters)

        # extract word from WordleWord object and convert to list
        ###char_list = list(wordle_game.user_attempt.wordle_word.word)#####
        char_list = ["T", "H", "E", "M", "E"]
        print(char_list)

        # convert user_guess to list
        user_guess_as_list = list(user_guess.upper())

        # create lists for correct_letters and misplaced_letters
        correct_letters = []
        misplaced_letters = []

        if user_guess_as_list == char_list:
            char_count = 0

            # update lbl_submitted_guess text
            label_text = f"Guess #{wordle_game.user_attempt.num_of_guesses} : {user_guess.upper()} is correct!"
            lbl_submitted_guess.config(text= label_text, fg="green")

            # update guess letter labels
            for char in user_guess_as_list:
                row_lbl_list = list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1]
                row_letter_lbl = row_lbl_list[char_count]
                row_letter_lbl.config(text=user_guess_as_list[char_count], fg='green', font='segoe 9 bold')
                row_lbl_list[char_count] = row_letter_lbl
                list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1] = row_lbl_list
                char_count += 1


            # update guessed_correct of attempt to True
            wordle_game.user_attempt.set_guessed_correct = True

            # update lbl_num_guessed_correct
            wordle_game.set_num_guessed_correct += 1
            lbl_num_guessed_correct.config(text= wordle_game.num_guessed_correct)

            # disable submit_btn and entry_guess
            submit_btn.config(state=DISABLED)
            entry_guess.config(state=DISABLED)

        #elif block for incorrect guess numbers less than MAX_GUESSES
        elif wordle_game.user_attempt.num_of_guesses < MAX_GUESSES:
            char_count = 0
            for char in user_guess_as_list:
                #check for correct letter
                if char_list[char_count] == user_guess_as_list[char_count]:

                    correct_letters.append(char)
                    # remove char from misplaced letters list if present
                    if char in misplaced_letters:
                        misplaced_letters.remove(char)

                    # update guess letter labels
                    row_lbl_list = list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1]
                    row_letter_lbl = row_lbl_list[char_count]
                    row_letter_lbl.config(text=user_guess_as_list[char_count], fg='green', font='segoe 9 bold')
                    row_lbl_list[char_count] = row_letter_lbl
                    list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1] = row_lbl_list

                    # replace current char in char_list with ""
                    char_list[char_count] = ""
                    print(char_list)

                    char_count += 1

                # check for misplaced letter
                elif char in char_list:
                    correct_letters.append("_")
                    misplaced_letters.append(char)

                    # update guess letter labels
                    row_lbl_list = list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1]
                    row_letter_lbl = row_lbl_list[char_count]
                    row_letter_lbl.config(text=user_guess_as_list[char_count], fg='orange', font='segoe 9 bold')
                    row_lbl_list[char_count] = row_letter_lbl
                    list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1] = row_lbl_list

                    # replace current char in char_list with ""
                    #char_list[char_count] = ""
                    print(char_list)

                    char_count += 1

                # char is not in word
                elif char not in char_list:
                    correct_letters.append("_")
                    wordle_game.user_attempt.wrong_letters.append(char)

                    # update guess letter labels
                    row_lbl_list = list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1]
                    row_letter_lbl = row_lbl_list[char_count]
                    row_letter_lbl.config(text=user_guess_as_list[char_count], fg="firebrick", font='segoe 9 bold')
                    row_lbl_list[char_count] = row_letter_lbl
                    list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1] = row_lbl_list

                    # replace current char in char_list with ""
                    #char_list[char_count] = ""
                    print(char_list)

                    char_count += 1

            # convert letter lists to sets to remove duplicates
            print("Incorrect")
            print(f"Correct Letters: {correct_letters}")
            print(f"Misplaced Letters: {set(misplaced_letters)}")
            print(f"Wrong Letters: {set(wordle_game.user_attempt.wrong_letters)}")

            # update letter_lbls that match wrong letters
            for letter in wordle_game.user_attempt.wrong_letters:
                temp_letter_lbl = letter_lbl_dict[letter]
                temp_letter_lbl.config(relief=SUNKEN, fg="red", font= 'segoe 9 bold')
                letter_lbl_dict[letter] = temp_letter_lbl

            # update lbl_submitted_guess text
            label_text = f"Guess #{wordle_game.user_attempt.num_of_guesses} : {user_guess.upper()} is incorrect"
            lbl_submitted_guess.config(text= label_text, fg="black")

        # else block for incorrect guess equaling MAX_GUESSES
        else:
            char_count = 0
            for char in user_guess_as_list:
                # check for correct letter
                if char_list[char_count] == user_guess_as_list[char_count]:

                    correct_letters.append(char)
                    # remove char from misplaced letters list if present
                    if char in misplaced_letters:
                        misplaced_letters.remove(char)

                    # update guess letter labels
                    row_lbl_list = list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1]
                    row_letter_lbl = row_lbl_list[char_count]
                    row_letter_lbl.config(text=user_guess_as_list[char_count], fg='green', font='segoe 9 bold')
                    row_lbl_list[char_count] = row_letter_lbl
                    list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1] = row_lbl_list

                    # replace current char in char_list with ""
                    char_list[char_count] = ""

                    char_count += 1

                # check for misplaced letter
                elif char in char_list:
                    correct_letters.append("_")
                    misplaced_letters.append(char)

                    # update guess letter labels
                    row_lbl_list = list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1]
                    row_letter_lbl = row_lbl_list[char_count]
                    row_letter_lbl.config(text=user_guess_as_list[char_count], fg='orange', font='segoe 9 bold')
                    row_lbl_list[char_count] = row_letter_lbl
                    list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1] = row_lbl_list

                    # replace current char in char_list with ""
                    char_list[char_count] = ""

                    char_count += 1

                # char is not in word
                elif char not in char_list:
                    correct_letters.append("_")
                    wordle_game.user_attempt.wrong_letters.append(char)

                    # update guess letter labels
                    row_lbl_list = list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1]
                    row_letter_lbl = row_lbl_list[char_count]
                    row_letter_lbl.config(text=user_guess_as_list[char_count], fg="firebrick", font='segoe 9 bold')
                    row_lbl_list[char_count] = row_letter_lbl
                    list_letter_row_lbls[wordle_game.user_attempt.num_of_guesses - 1] = row_lbl_list

                    # replace current char in char_list with ""
                    char_list[char_count] = ""

                    char_count += 1

            # convert letter lists to sets to remove duplicates
            print("Incorrect")
            print(f"Correct Letters: {correct_letters}")
            print(f"Misplaced Letters: {set(misplaced_letters)}")
            print(f"Wrong Letters: {set(wordle_game.user_attempt.wrong_letters)}")

            # update letter_lbls that match wrong letters
            for letter in wordle_game.user_attempt.wrong_letters:
                temp_letter_lbl = letter_lbl_dict[letter]
                temp_letter_lbl.config(relief=SUNKEN, fg="red", font='segoe 9 bold')
                letter_lbl_dict[letter] = temp_letter_lbl

            # update lbl_submitted_guess text
            lbl_submitted_guess.config(text=f"Incorrect, Correct word was{char_list}", fg="red")

def gen_next_word_attempt():
    """
    This method resets the necessary GUI labels and creates a new Attempt object.
    :return:
    """
    # update necessary GUI letter labels before creating new attempt
    for letter in wordle_game.user_attempt.wrong_letters:
        temp_letter_lbl = letter_lbl_dict[letter]
        temp_letter_lbl.config(relief=FLAT, fg="black", font='segoe 9 normal')
        letter_lbl_dict[letter] = temp_letter_lbl
    for label_list in list_letter_row_lbls:
        for label in label_list:
            label.config(text="_", fg="black", font="segoe 9 normal")

    # create new attempt
    wordle_game.generate_random_attempt()
    # print(wordle_game.user_attempt.wordle_word.word)

    # update lbl_current_word_num field and wordle_game number of games attempted
    lbl_current_word_num.config(text=wordle_game.num_of_words_attempted)

    # enable submit_btn and entry_guess
    submit_btn.config(state=NORMAL)
    entry_guess.config(state=NORMAL)

'''
FUNCTIONS ABOVE HERE
'''
main_window = tk.Tk()

your_font = font.nametofont("TkDefaultFont")  # Get default font value into Font object
print(your_font.actual())

'''
MODULE CODE BELOW HERE
'''

# set title of main_window
main_window.title("CIS189 Wordle Game")

# set default size of main window
main_window.geometry("900x575")

# create variables for grid limits
row_limit = 23
col_limit = 12

# create variable for column width
col_width = 10

# add empty labels for grid limits
lbl_empty_row_limit = tk.Label(main_window, text='')
lbl_empty_row_limit.grid(row=row_limit, column=1)

lbl_empty_col_limit = tk.Label(main_window, text='')
lbl_empty_col_limit.grid(row=0, column=col_limit)

# set column width
set_col_width(col_limit, col_width)

# add empy label for row 1
lbl_empty_row1 = tk.Label(main_window, text='')
lbl_empty_row1.grid(row=1, column=0)

# create letter labels top of GUI
create_row_letter_labels()

# test print to ensure 26 different letter labels added to letter_lbl_dict
#print(len(letter_lbl_dict))

# create guess labels
create_guess_labels()

# add empty label for row 5
lbl_empty_row5 = tk.Label(main_window, text='')
lbl_empty_row5.grid(row=5, column=0)

# add empty label for row 7
lbl_empty_row7 = tk.Label(main_window, text='')
lbl_empty_row7.grid(row=7, column=0)

# add empty label for row 9
lbl_empty_row9 = tk.Label(main_window, text='')
lbl_empty_row9.grid(row=9, column=0)

# add empty label for row 11
lbl_empty_row11 = tk.Label(main_window, text='')
lbl_empty_row11.grid(row=11, column=0)

# add empty label for row 13
lbl_empty_row13 = tk.Label(main_window, text='')
lbl_empty_row13.grid(row=13, column=0)

#print(len(list_letter_row_lbls))

# add empty label for row 15
lbl_empty_row15 = tk.Label(main_window, text='')
lbl_empty_row15.grid(row=15, column=0)

# add empty label for row 16
lbl_empty_row16 = tk.Label(main_window, text='')
lbl_empty_row16.grid(row=16, column=0)

# create "Word#" label and current word number field in row 17
lbl_static_word_num = tk.Label(main_window, text="Word # :", justify="right")
lbl_static_word_num.grid(row=17, column=1, rowspan=1, columnspan=1)

lbl_current_word_num = tk.Label(main_window, text="")
lbl_current_word_num.grid(row=17, column=2, rowspan=1, columnspan=1)

# create "Enter Guess" label and text entry field in row 17
lbl_enter_guess = tk.Label(main_window, text="Enter Guess:", justify="right")
lbl_enter_guess.grid(row=17, column=3, rowspan=1, columnspan=2)

entry_guess = tk.Entry(main_window, width=20, justify="center", state=DISABLED)
entry_guess.grid(row=17, column=5, rowspan=1, columnspan=2)

# create "Guessed Correctly" label and number of correctly guess field/label in row 17
lbl_guessed_correctly = tk.Label(main_window, text="Guessed Correctly:", justify="right")
lbl_guessed_correctly.grid(row=17, column=8, rowspan=1, columnspan=2)

lbl_num_guessed_correct = tk.Label(main_window, text="", justify="right")
lbl_num_guessed_correct.grid(row=17, column=10, rowspan=1, columnspan=1)

# add empty label for row 18
lbl_empty_row18 = tk.Label(main_window, text='')
lbl_empty_row18.grid(row=18, column=0)

# add Next Word button to row 19
next_word_btn= tk.Button(main_window, text="Next Word", state=DISABLED, command=lambda: gen_next_word_attempt())
next_word_btn.grid(row=19, column=1, rowspan=1, columnspan=2)

# add Submit Button to row 19
submit_btn = tk.Button(main_window, text="Submit", width=25, justify="center", state=DISABLED, command=lambda: submit_guess())
submit_btn.grid(row=19, column=5, rowspan=1, columnspan=2)

# add empty label for row 20
lbl_empty_row20 = tk.Label(main_window, text='')
lbl_empty_row20.grid(row=20, column=0)

# add Start Game Button to row 21
start_game_btn = tk.Button(main_window, text="Start Game", command= lambda : start_game())
start_game_btn.grid(row= 21, column=2, rowspan=1, columnspan=1)

# add submitted_guess label to row 21
lbl_submitted_guess = tk.Label(main_window, text="")
lbl_submitted_guess.grid(row=21, column=4, rowspan=1, columnspan=4)

# create Quit Game button to row 21
quit_btn = tk.Button(main_window, text="Quit Game", command=main_window.destroy)
quit_btn.grid(row=21, column=9, rowspan=1, columnspan=1)

# add empty label for row 22
lbl_empty_row22 = tk.Label(main_window, text='')
lbl_empty_row22.grid(row=22, column=0)

'''
MODULE CODE ABOVE HERE
'''

# run main_window.mainloop()
main_window.mainloop()