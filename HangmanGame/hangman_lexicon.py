import random


class Lexicon(object):
#Choose the word for play
    def choose_word(self, level):
        if level == 1:
            with open("data/Lexikon1.txt") as words:
                words = words.readlines()
        elif level==0:
            with open("data/Lexikon2.txt") as words:
                words = words.readlines()
        lexicon = [x.strip().split() for x in words]
        chosen_word = random.choice(lexicon)
        return chosen_word[0]

