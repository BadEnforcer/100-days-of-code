import tkinter

window = tkinter.Tk()
window.config(padx=10, pady=10)
# Entry and text on left
MILES = tkinter.Entry(width=10)
MILES.grid(column=2, row=0, pady=20, padx=10)


def convert():
    km.config(text=round(float(MILES.get()) * 1.60934, 2))


# row 1
miles_text = tkinter.Label(text="Miles", font=("Aerial", 10, "normal"))
miles_text.grid(column=3, row=0)
# row 2
equal_text = tkinter.Label(text="is equal to")
equal_text.grid(column=1, row=1)
km = tkinter.Label(text=0)
km.grid(column=2, row=1)

km_text = tkinter.Label(text="Km")
km_text.grid(column=3, row=1)

# calculate
button = tkinter.Button(text="Calculate", command=convert)
button.grid(column=2, row=2)
tkinter.mainloop()
