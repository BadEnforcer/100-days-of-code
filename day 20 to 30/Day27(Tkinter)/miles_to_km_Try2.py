import tkinter

window = tkinter.Tk()
window.title("Miles to Kilometers")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


# def convert(*args):  # use *args or *kwargs . can also use an index
#     finish(int(entry.get()))
#

def finish():
    miles = entry.get()
    km = round(float(miles) * 1.609,2)
    result = tkinter.Label(text=f"{km}", font=("Times New Roman", 16, "normal"))
    result.grid(row=1, column=1)




# Miles text
M = tkinter.Label(text="Miles", font=("Times New Roman", 16, "normal"))
M.grid(row=0, column=2)

# Entry
entry = tkinter.Entry(width=10)
entry.grid(row=0, column=1)

# is equal to
IE = tkinter.Label(text="is Equal to", font=("Times New Roman", 16, "normal"))
IE.grid(row=1, column=0)
# km

km = tkinter.Label(text="KM", font=("Times New Roman", 16, "normal"))
km.grid(row=1, column=2)


# button
button = tkinter.Button(text="Convert!", font=16, command=finish)
button.grid(row=2, column=1)



window.mainloop()  # at the very end
