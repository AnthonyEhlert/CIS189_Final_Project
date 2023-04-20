"""
Program: WordleWord.py
Author: Tony Ehlert
Last date modified: 4/21/2023

The purpose of this program is to define a WordleWord class to be used within a Wordle guessing game
The input is required information and code to define the class
The output is print statements to the console to test the class
"""
class WordleWord():
    def __init__(self, word):
        # create superset for validating word attribute
        word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

        # check to ensure no numbers are in word
        if not word_characters.issuperset(word):
            raise ValueError

        # check to ensure word is correct length
        if len(word) != 5:
            raise ValueError

        self._word = str(word).upper()
        self._attempted = False

    # GETTERS AND SETTERS
    @property
    def word(self):
        return self._word
    
    @word.setter
    def set_word(self, word):
        # create superset for validating word attribute
        word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

        # check to ensure no numbers are in word
        if not word_characters.issuperset(word):
            raise ValueError

        # check to ensure word is correct length
        if len(word) != 5:
            raise ValueError
        self._word = word
        
    @property
    def attempted(self):
        return self._attempted
    
    @attempted.setter
    def set_attempted(self, attempted):
        self._attempted = attempted

    def __str__(self):
        str_string = f"Wordle Word(Word: \"{self._word}\", Attempted: {self._attempted})"
        return str_string

    def __repr__(self):
        repr_string = f"WordleWord(\"" + self._word + "\")"
        return repr_string




# Driver/Main
if __name__ == "__main__":
    # create test WordleWord object
    test_wordle_word = WordleWord("trust")

    # test __str__ and __repr__ methods
    print(test_wordle_word)
    print(test_wordle_word.__repr__())

    # garbage collection
    del test_wordle_word
