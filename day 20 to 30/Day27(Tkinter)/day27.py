import tkinter


def is_clicked():
    print("it clicked")
    # a_input = input.get()
    my_label["text"] = "Poof!"  # or
    # my_label.config(text=a_input)
# we use pack, place and grid || with place, x and y cor are required.
# and grid requires column and row value. row starts from 0, or we can start from 1 also.
# we can use grid and pack together


window = tkinter.Tk()
window.title("Test")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # add extra space around things.
# if we want to add padding into a specific thing. instead of window use that specific item.

# Label
my_label = tkinter.Label(text="i am label", font=("Aerial", 20, "normal"))
my_label.grid(column=1, row=1)  # show in screen # imp

# button


my_button = tkinter.Button(text="Click", command=is_clicked)
my_button.grid(column=2, row=2)

# test button
test_b = tkinter.Button(text="This is a test. uwu")
test_b.grid(column=3, row=1)


# Entry (input)
a_input = tkinter.Entry(width=10)
a_input.grid(column=4, row=4)

window.mainloop()  # has to be in the end
