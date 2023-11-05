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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        reps = 0
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
    else:
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pamadoro")
window.config(padx=100, pady=50, bg=YELLOW)

# LABELS
title_label = Label(text="Timer", font=(
    FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)


check_marks_label = Label(text="✔", font=(
    FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
# check_marks_label.grid(row=3, column=1)

# CANVAS
# highlightthickness = 0 will get rid of the border left when changing the bg
canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato-s.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
# Buttons
start_btn = Button(text="Start", borderwidth=0,
                   highlightthickness=0, padx=3, pady=3, command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", borderwidth=0,
                   highlightthickness=0, padx=3, pady=3)
reset_btn.grid(row=2, column=2)

window.mainloop()
