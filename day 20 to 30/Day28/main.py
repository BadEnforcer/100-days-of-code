from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

work_sec = WORK_MIN * 60
short_break_sec = SHORT_BREAK_MIN * 60
long_break_sec = LONG_BREAK_MIN * 60

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    window.after_cancel(timer)
    top_label.config(text="Timer", fg=GREEN)
    check_box.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        top_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        top_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        top_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = (count % 60)
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        mark = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            mark += "✔"
        check_box.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# photo image
tomato = PhotoImage(file="tomato.png")
# canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 20, "bold"), fill="white")  # Timer
canvas.grid(row=1, column=1)

top_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
top_label.grid(row=0, column=1)

# start button
start_button = Button(text="Start", font=(FONT_NAME, 10, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "normal"), command=reset, highlightthickness=0)
reset_button.grid(row=2, column=2)

# check_box
check_box = Label(font=(FONT_NAME, 9, "normal"), bg=YELLOW, fg=GREEN)
check_box.grid(row=3, column=1)

# count_down(5)
window.mainloop()
