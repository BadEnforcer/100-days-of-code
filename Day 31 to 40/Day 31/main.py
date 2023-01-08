from random import choice
import pandas
from tkinter import *


# TODO : pandas stuff is bit messed up. need to be cleaned up.

# constant
BACKGROUND_COLOR = "#B1DDC6"
Data_File = "./data/french_words.csv"
Bold_font = ("Raleway Bold", 60, "normal")
italic_font = ("Cronus italic", 40, "normal")
FRONT_CARD = ".static/images/card_front.png"
BACK_CARD = ".static/images/card_back.png"
Yes_img_path = ".static/images/right.png"
No_img_path = ".static/images/wrong.png"

# pandas
word_database = pandas.read_csv(Data_File)
English_words = word_database["English"]
French_words = word_database["French"]
# we can use data_to_dict() option and use the  orient argument in pandas also.

# lists
completed_word_indexes = []
global_index = []


def random_index():
    num = choice(range(0, len(word_database["French"])))
    return num


def run():
    global global_index, flip_timer
    word_index = random_index()
    window.after_cancel(flip_timer)  # will flip through this line

    for banned_index in completed_word_indexes:
        if banned_index == word_index:
            random_index()
    global_index = random_index()
    white_screen(word_index)
    flip_timer = window.after(3000, green_screen, global_index)


def white_screen(word_index):
    # change bg
    canvas.itemconfig(card_image, image=front_card)

    # configure text
    canvas.itemconfig(language, text="French", fill="#000000")
    canvas.itemconfig(written_word, text=French_words[word_index], fill="#000000")
    # we can also use "black" or "white" instead of hex codes


def green_screen(w_index):  # flips the card
    canvas.itemconfig(card_image, image=back_card)
    canvas.itemconfig(language, text="English", fill="#FFFFFF")
    canvas.itemconfig(written_word, text=English_words[w_index], fill="#FFFFFF")


def yes_sign():
    completed_word_indexes.append(global_index)
    df = pandas.DataFrame({'': [(len(completed_word_indexes))],
                           "Word": French_words[global_index]})
    df.to_csv("./data/completed_words.csv", mode='a', index=False, header=False)
    # print(df)
    run()


def no_sign():
    run()


# setting up tkinter

window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# UI Setup

front_card = PhotoImage(file=FRONT_CARD)
back_card = PhotoImage(file=BACK_CARD)

# canvas
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263)
language = canvas.create_text(400, 150, font=italic_font)
written_word = canvas.create_text(400, 263, font=Bold_font)

canvas.grid(row=0, column=0, columnspan=2)

known_image = PhotoImage(file=Yes_img_path)
unknown_image = PhotoImage(file=No_img_path)

known_button = Button(image=known_image, command=yes_sign, highlightthickness=0)
known_button.grid(row=1, column=0)

unknown_button = Button(image=unknown_image, command=no_sign, highlightthickness=0)
unknown_button.grid(row=1, column=1)

flip_timer = window.after(3000, green_screen, global_index)

run()

window.mainloop()
