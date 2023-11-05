from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

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
canvas.create_text(100, 112, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Buttons
# Buttons
start_btn = Button(text="Start", borderwidth=0,
                   highlightthickness=0, padx=3, pady=3)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", borderwidth=0,
                   highlightthickness=0, padx=3, pady=3)
reset_btn.grid(row=2, column=2)

window.mainloop()
