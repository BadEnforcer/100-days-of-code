import random
from tkinter import *
from tkinter import messagebox
import sv_ttk
from tkinter import ttk
import json

# CONSTANTS
Data_File = "test.json"
FONT = ("Times New Roman", 10, "normal")

numbers = ["1", "2", "3", "4", "4", "5", "6", "7", "8", "8", "9", "0"]
special_chars = ["!", "#", "$", "%", "&", "'", "*", "0", ".", "/", "<", "=", ">", "?", "@", "^", "_",
                 "`", "|", "~", ")"]
small_alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "solution", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
capital_alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z"]


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    Passwd_Entry.delete(0, END)
    # number
    passwd_num = [random.choice(numbers) for _ in range(2)]
    passwd_special_char = [random.choice(special_chars) for _ in range(2)]
    passwd_sa = [random.choice(small_alphabets) for _ in range(1)]
    passwd_ca = [random.choice(capital_alphabets) for _ in range(3)]
    # password
    passwd = passwd_num + passwd_special_char + passwd_sa + passwd_ca
    random.shuffle(passwd)
    pass_string = "".join(passwd)
    t_password.set(value=pass_string)
    print(t_website.get())
    print(t_password.get())
    print(t_email.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title("MyPass")
window.config(padx=200, pady=200)
sv_ttk.set_theme("dark")
sv_ttk.use_dark_theme()

# vars
t_website = StringVar()
t_password = StringVar()
t_email = StringVar(value="Rajdwivedipc@gmail.com")


def save():
    if t_password.get() == "" or t_email.get() == "" or t_website == "":
        messagebox.showerror(title="Missing Data", message="Please Don't Leave Any fields Empty !")
    else:
        new_data = {
            t_website.get(): {
                "email/username": t_email.get(),
                "password": t_password.get()
            }
        }
        try:
            with open(Data_File, "r") as datafile:
                data = json.load(datafile)
        except FileNotFoundError:
            with open(Data_File, "w") as df:
                json.dump(new_data, df, indent=4)
        else:
            data.update(new_data)
            with open(Data_File, "w") as df:
                json.dump(data, df, indent=4)
        # finally:
        messagebox.showinfo(title="Save information", message="Details added to the DataBase!.")
        window.clipboard_clear()
        window.clipboard_append(t_password.get())
        Website_Entry.delete(0, END)
        Passwd_Entry.delete(0, END)


def find_pass():
    try:
        with open(Data_File, "r") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="DataBase File Does not Exist in the directory")
    try:
        website = data[t_website.get()]
        messagebox.showinfo(title=f"Details for {t_website.get()}", message=
        f"Email/Username : {website['email/username']}\nPassword : {website['password']}")
    except KeyError:
        messagebox.showerror(title="Error", message="No Details Found")


# Canvas
main_canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="../Day29/logo.png")
main_canvas.create_image(100, 100, image=logo)
main_canvas.grid(row=0, column=1)

# Labels
Website_label = ttk.Label(text="Website :", font=FONT)
Email_or_username_label = ttk.Label(text="Email/Username :", font=FONT)
Passwd_label = ttk.Label(text="Password :", font=FONT)

Website_label.grid(row=1, column=0, padx=20, pady=3)
Email_or_username_label.grid(row=2, column=0, pady=3)
Passwd_label.grid(row=3, column=0, padx=20, pady=3)

# Entry
Website_Entry = ttk.Entry(textvariable=t_website, width=30)
Email_Entry = ttk.Entry(textvariable=t_email, width=51)
Passwd_Entry = ttk.Entry(textvariable=t_password, width=25)

Website_Entry.grid(row=1, column=1, pady=3, sticky=W)
Website_Entry.focus()
Email_Entry.grid(row=2, column=1, pady=3, sticky=W)
Passwd_Entry.grid(row=3, column=1, pady=3, sticky=W)

# generate button
find_button = ttk.Button(text="Find", command=find_pass, width=15)
find_button.grid(row=1, column=1, pady=3, sticky=E)
make_passwd = ttk.Button(text="Generate Password", command=generate)
make_passwd.grid(row=3, column=1, pady=3, sticky=E)
add_details = ttk.Button(text="Add", width=50, command=save)
add_details.grid(row=4, column=1, pady=3, sticky=W)

window.mainloop()
