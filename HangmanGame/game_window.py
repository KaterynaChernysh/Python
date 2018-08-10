import Tkinter as Tk
import tkMessageBox

from game_rules import *
from hangman_man import *
import turtle

# import hangman
import hangman_lexicon


class NimGui(object):
    button_mapping = {}
    gameRules = GameRules()  #start part
    lexicon = Lexicon()

    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.image_size = 550, 480
        self.rules = Tk.IntVar()
        self.rules.set(0)
        self.game_started = False
        self.window()
        self.menubar()

    def window(self):
#Welcometext
        top_frame = Tk.Frame(self.root)
        top_frame.grid(row=0, column=0, sticky="w", padx=5, pady=5, columnspan=2)
        top_frame.grid_columnconfigure(1, weight=2)
        welcome_word = Tk.Label(top_frame, text="Welcome to the Hangman Game! Are you ready to die?")
        welcome_word.grid(row=0, column=0, sticky="w")

#Picture of Hangman
        mid_frame1 = Tk.Frame(self.root)
        mid_frame1.grid(row=1, sticky="w")
        self.label_box = Tk.Label(master=mid_frame1)
        # self.label_box.image = im
        self.label_box.grid(row=1, padx=5, sticky="w")
        self.label_box.grid_columnconfigure(1, weight=1)
        canvas = Tk.Canvas(master=self.label_box, width=500, height=500)
        canvas.pack()
        self.t = turtle.RawTurtle(canvas)
        draw_background(self.t)

#Shows the word and "Right" / "Flase" in different cases
        mid_frame2 = Tk.Frame(self.root)
        mid_frame2.grid(row=1, column=1, sticky="w")
        mid_frame2.grid_columnconfigure(1,weight=1)

        # current_word = hangmanGame.Lexicon.lexicon_beginners
#Choose the word for play

        self.guessed_word = Tk.Label(mid_frame2, text = self.gameRules.get_secret_word())   #start part
        self.guessed_word.grid(row=0, padx=5, sticky="ew")
        self.guessed_word.grid_columnconfigure(1, weight=1)

        self.guess_match = Tk.Label(mid_frame2, text="")
        self.guess_match.grid(row=1, padx=5, sticky="ew")
        self.guess_match.grid_columnconfigure(1,weight=1)

#Letter-buttons
        mid_frame3 = Tk.Frame(self.root)
        mid_frame3.grid(row=1, column=2, sticky="w", padx=5, pady=5)
        letter = 64    #65-90
        alphabet = []
        letter_button = []
        for i in range(5):
            alphabet.append([])
            letter_button.append([])
            for j in range (5):
                alphabet[i].append(chr(letter))
                letter += 1
                b = Tk.Button(mid_frame3, text=chr(letter))
                b.bind("<Button-1>", self.button_click)
                self.button_mapping[b] = chr(letter)
                letter_button[i].append(b)
                letter_button[i][j].grid(row=i, column=j, padx=5, sticky="ew")
                letter_button[i][j].grid_columnconfigure(1, weight=1)
                letter_button[i][j].bind(chr(letter))

        z = Tk.Button(mid_frame3, text="Z")
        z.bind("<Button-1>", self.button_click)
        self.button_mapping[z] = chr(90)
        z.grid(row=5, column=2, padx=5, sticky="ew")
        z.grid_columnconfigure(1,weight=1)

#Used Letters
        bottom_frame = Tk.Frame(self.root)
        bottom_frame.grid(row=2, column=2, sticky="n", padx=5, pady=5)
        self.used_letters = Tk.Label(bottom_frame, bg="white", borderwidth = 2, relief=Tk.GROOVE)
        self.used_letters.grid(row=2, padx=5, sticky="w")
        self.used_letters.grid_columnconfigure(1, weight=1)

    def button_click(self, event):
        letter = self.button_mapping[event.widget]
        text = self.used_letters.cget("text")
        self.used_letters.config(text = text + " " + letter)

        state = self.gameRules.guess(letter)
        self.guessed_word.config(text = self.gameRules.get_secret_word())

        if state == GameRules.STATE_WIN:
            self.guess_match.config(text = "WIN!")
        elif state == GameRules.STATE_LOOSE:
            self.guess_match.config(text="LOOSE!")
            guesses = self.gameRules.get_guesses_cnt()
            draw_man(self.t, guesses)
        elif state == GameRules.STATE_SAME:
            self.guess_match.config(text="SAME!")
        elif state == GameRules.STATE_WRONG:
            self.guess_match.config(text="WRONG!")
            guesses = self.gameRules.get_guesses_cnt()
            draw_man(self.t, guesses)
        elif state == GameRules.STATE_RIGHT:
            self.guess_match.config(text="RIGHT!")
        return

    def start(self):
        return

    def stop(self):
        self.game_started = False
        return

    def menubar(self):
        menu_main = Tk.Menu(self.root)
        menu_start = Tk.Menu(menu_main, tearoff = 0)
        menu_options = Tk.Menu(menu_main, tearoff=0)
        menu_help = Tk.Menu(menu_main, tearoff=0)
        # menu_start.add_radiobutton(label = "Start", underline = 0, command = self.start)
        menu_options.add_radiobutton(label="Grundwortschatz fuer die Jahrgangsstufen 1 und 2", value=0, variable=self.gameRules.level)
        menu_options.add_radiobutton(label="Grundwortschatz fuer die Jahrgangsstufen 3 und 4", value=1, variable=self.gameRules.level)
        help_text = ("Hangman Game for people who try to learn german\n"
                     "Analysieren und Visualisieren mit Python WS1718\n"
                     "Informationswissenschaft\n"
                     "Uni Regensburg\n"
                     "Chernysh Kateryna, Dudyka Maria-Theresia")
        menu_help.add_command(label = "About the Game", underline = 0, command = lambda : tkMessageBox.showinfo("HMG", help_text))
        # menu_start.add_cascade(label = "Start", underline = 0, menu=menu_start)
        menu_start.add_command(label="Start", underline = 0, command=self.start)
        menu_main.add_cascade(label="Start", underline=0, menu=menu_start)
        menu_main.add_cascade(label = "Lexicon", underline = 0, menu = menu_options)
        menu_main.add_cascade(label = "Help", underline = 0, menu = menu_help)

        self.root.config(menu = menu_main)


r = Tk.Tk()
NimGui(r)
r.mainloop()