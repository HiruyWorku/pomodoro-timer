import tkinter as tk
import math

WORK = 25 * 60  # Duration of work in seconds
SHORT_BREAK = 5 * 60  # Duration of a short break in seconds
LONG_BREAK = 20 * 60  # Duration of a long break in seconds
REPITITION = 0  # Number of completed work sessions
TIMER = None

# Define the number of work sessions before a long break
SESSIONS_BEFORE_LONG_BREAK = 4

def timer_reset():
    global REPITITION
    REPITITION = 0
    start_button["state"] = 'normal'
    root.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00", fill="#A020F0")
    check_marks.config(text="")

def start_timer():
    start_button["state"] = "disabled"
    countdown(WORK)
    
def switch_to_short_break():
    global REPITITION
    REPITITION += 1
    if REPITITION % SESSIONS_BEFORE_LONG_BREAK == 0:
        countdown(LONG_BREAK)
    else:
        countdown(SHORT_BREAK)

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global TIMER
        TIMER = root.after(1000, countdown, count - 1)
    else:
        switch_to_short_break()
        marks = "✓" * (REPITITION // 2)  # Add checkmarks based on completed work sessions
        check_marks.config(text=marks)

root = tk.Tk()
root.title("Hiruys POMODORO")
root.config(padx=100, pady=50, bg="#f7f5dd")

title_label = tk.Label(text="TIMER", fg='#A020f0', bg='#f7f5dd', font=("Arial", 50))
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer, bg="#e7305b", font=("Arial", 15, "bold"))
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=timer_reset, bg="#e7305b", font=("Arial", 15, "bold"))
reset_button.grid(column=2, row=2)

check_marks = tk.Label(text="", fg='#00FF00', bg="#f7f5dd", font=("Arial", 25, "bold"))
check_marks.grid(column=1, row=3)

root.mainloop()
