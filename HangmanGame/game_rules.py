from hangman_lexicon import *
from hangman_man import *
from hangman_lexicon import *


class GameRules(object):

    TRIES_COUNT = 6

    STATE_WIN = 1
    STATE_LOOSE = 2
    STATE_RIGHT = 3
    STATE_WRONG = 4
    STATE_SAME = 5

    def __init__(self):
        self.lexicon = Lexicon()
        self.guesses = 0
        self.level = 0
        chosen_word = self.lexicon.choose_word(self.level)
        # chosen_word = "Beispiel"
        self.chosen_word_letters = list(chosen_word.upper())
        self.guessed_letters = []
        self.guessed_letters_cnt = 0 # with repeats
        self.chosed_letters = []
        self.secret_word = []
        self.calculate_secret_word()

        # ----
        # print(self.chosen_word_letters)
        # print(self.get_secret_word())
        # print(self.guess('k'))
        # print(self.guess('k'))
        # print(self.get_secret_word())
        # print(self.guess('f'))
        # print(self.guess('v'))
        # print(self.guess('z'))
        # print(self.guess('f'))
        # print(self.guess('b'))
        # print(self.guess('p'))
        # print(self.get_secret_word())

    def calculate_secret_word(self):
        self.secret_word = []
        self.guessed_letters_cnt = 0
        for letter in self.chosen_word_letters:
            if letter in self.guessed_letters:
                self.secret_word.append(letter)
                self.guessed_letters_cnt += 1
            else:
                self.secret_word.append('?')

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.chosed_letters:
            return self.STATE_SAME

        self.chosed_letters.append(letter)

        if letter in self.chosen_word_letters:
            self.guessed_letters.append(letter)
            self.calculate_secret_word()
            if self.guessed_letters_cnt == len(self.chosen_word_letters):
                return self.STATE_WIN
            else:
                return self.STATE_RIGHT
        else:
            self.guesses += 1
            if self.guesses == self.TRIES_COUNT:
                return self.STATE_LOOSE
            else:
                return self.STATE_WRONG

    def get_secret_word(self):
        return self.secret_word

    def get_guesses_cnt(self):
        return self.guesses