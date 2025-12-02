import tkinter
import random

screen = tkinter.Tk()
screen.geometry("400x400")

words = [
"egg", "pan", "chicken", "hen", "farm", "chick", "hill"
"sunny", "sun", "day", "coop", "seed", "feather", "lawn"
"meat", "rooster", "yolk", "ground", "sky", "cloud",
"bird", "mud", "dirt", "grass", "beak", "wing", "night",
"moon", "white", "brown", "black", "barn", "house",
"fence", "gate", "wood", "paint", "flower", "pollen",
"bee", "honey", "river", "lake", "water", "wheat", "grain",
"bone", "blood", "stove", "lunch", "breakfast", "dinner",
"rainbow", "country", "land", "territory", "dream", "bed",
"sleep", "kitchen", "room", "knife", "fork", "spoon",
"tablecloth", "cloth", "table", "chair", "floor", "ceiling",
"sheep", "pig", "dog", "horse", "cat", "donkey", "goat",
"ketchup", "mustard", "mayonaise", "radio", "television",
"fan", "door", "window", "mirror", "remote", "snow", "ice"
    ]

word = ""

total = 0
score = 0


def refresh_score():
    global score
    global total

    score_l.config(text=f"Score: {score}/{total}")


def scramble_word():
    global word

    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    jumb_word.config(text=scrambled)
    words.remove(word)


def guess_word():
    global word
    guess = guess_input.get()

    global score
    global total

    if guess.lower() == word:
        score += 1
        total += 1
    else:
        total += 1
    refresh_score()
    answer_l.config(text=f"Prev Ans: {word}")
    scramble_word()
    guess_input.delete(0, tkinter.END)


def btn_guess_word():
    guess_word()


def bind_guess_word(event):
    guess_word()
    

title = tkinter.Label(screen, text="Jumbled Word Game", font="arial 18 normal")
jumb_word = tkinter.Label(screen, text="", font="arial 13 normal")
guess_input = tkinter.Entry(screen, font="arial 14 normal")
guess_btn = tkinter.Button(screen, text="Accept", command=btn_guess_word)
answer_l = tkinter.Label(screen, text="Unscramble the Word")
score_l = tkinter.Label(screen, text="Score: 0/0")

scramble_word()

screen.bind("<Return>", bind_guess_word)  # Enter is when mouse enters screen.

title.pack(pady=10)
jumb_word.pack()
guess_input.pack()
guess_input.pack()
guess_btn.pack()
answer_l.pack()
score_l.pack(pady=5)

screen.mainloop()
