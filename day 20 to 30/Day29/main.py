import random
from tkinter import *

# CONSTANTS
Data_File = None

# functions

def init():
    generate(pass_word=password, pass_length=password_length, num_length=numbers_length,
             special_char_length=no_of_special_chars, use_nums=include_numbers,
             use_caps=include_caps, use_small=include_lowercase, use_symbol=include_symbols,
             hide_brackets=exclude_brackets)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
special_chars = ["!", "#", "$", "%", "&", "'", "*", "0", ".", "/", "<", "=", ">", "?", "@", "\",""^", "_",
                 "`", "|", "~", ")"]

special_bracket_chars = ["!", "#", "$", "%", "&", "'", "*", "0", ".", "/", "<", "=", ">", "?", "@", "\",""^", "_",
                         "`", "|", "~", ")", "(", ")", "{", "}"]
small_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "solution", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
capital_alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z"]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate(pass_word, pass_length, num_length, special_char_length, use_nums, use_caps, use_small, use_symbol,
             hide_brackets):
    # generate numbers
    if use_nums:
        for _ in range(num_length.get() - 1):
            pass_word += str(random.choice(numbers))

    # generate symbols
    if use_symbol and hide_brackets:
        for _ in range(special_char_length.get() - 1):
            pass_word += random.choice(special_chars)

    elif use_symbol and hide_brackets is False:
        for _ in range(special_char_length.get() - 1):
            pass_word += random.choice(special_bracket_chars)

    # generate alphabets

    if use_caps and use_small:
        for _ in range(pass_length.get() - (numbers_length.get() + no_of_special_chars.get())):
            pass_word += random.choice(small_alphabets and capital_alphabets)

    elif use_caps and use_small is False:
        for _ in range(pass_length.get() - (numbers_length.get() + no_of_special_chars.get())):
            pass_word += random.choice(capital_alphabets)
    elif use_caps is False and use_small:
        for _ in range(pass_length.get() - (numbers_length.get() + no_of_special_chars.get())):
            pass_word += random.choice(small_alphabets)
    print(pass_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("MyPass")
window.config(padx=500, pady=100)

password = []
password_length = IntVar()
numbers_length = IntVar()
no_of_special_chars = IntVar()
include_numbers = BooleanVar()
include_caps = BooleanVar()
include_lowercase = BooleanVar()
include_symbols = BooleanVar()
exclude_brackets = BooleanVar()

# value checkboxes
caps_checkbox = Checkbutton(window, text="Include Caps", variable=include_caps, onvalue=1, offvalue=0, height=5,
                            width=20)
lowercase_checkbox = Checkbutton(window, text="Include Lower Case", variable=include_lowercase, onvalue=1, offvalue=0,
                                 height=5, width=20)
symbols_checkbox = Checkbutton(window, text="Include Symbols", variable=include_symbols, onvalue=1, offvalue=0,
                               height=5, width=20)
numbers_checkbox = Checkbutton(window, text="Include Numbers", variable=include_numbers, onvalue=1, offvalue=0,
                               height=5, width=20)
brackets_checkbox = Checkbutton(window, text="Exclude Brackets", variable=exclude_brackets, onvalue=1, offvalue=0,
                                height=5, width=20, command=init)

caps_checkbox.pack()
lowercase_checkbox.pack()
numbers_checkbox.pack()
symbols_checkbox.pack()
brackets_checkbox.pack()

password_length.set(8)
numbers_length.set(2)
no_of_special_chars.set(2)




window.mainloop()
