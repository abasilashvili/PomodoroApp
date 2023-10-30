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

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer_text
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text=" ")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_timer = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps == 8:
        title_label.config(text="Long break", fg=RED)
        count_down(long_break)

    elif reps%2 == 0 and reps != 0:
        title_label.config(text="Short break", fg=PINK)
        count_down(short_break)
        reps +=1

    elif reps%2 > 0 or reps == 0:
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_timer)
        reps +=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_min < 1 and count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
    mark = " "
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
        mark += "✓"
    check_marks.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("FONT_NAME", 35, "bold"))
title_label.grid(column=2, row=1)

canvas = Canvas(width=250, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("FONT_NAME", 35, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(35))
check_marks.grid(column=2, row=3)

window.mainloop()
