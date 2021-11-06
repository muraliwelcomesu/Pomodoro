from tkinter import *
import math
import Notify as msg
'''
The Pomodoro technique is an efficient system of time management. 
Where instead of multitasking a person focuses on a particular task at the given moment.
We focus on the task for 25 straight minutes and then after take a 5 minute break.
 A time sprint of 30 Minutes which is termed as a single Pomodoro. 
 After 4 such Pomodoros the user takes a longer break of 20 minutes.
 https://www.youtube.com/watch?v=mNBmG24djoY
'''
def Notify(message):
    msg.beep()
    msg.text_notify(message)
    #msg.voice_notify(message)


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
g_reset = 0
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global g_reset
    g_reset = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global g_reset
    if g_reset < 1 :
        g_reset = 1 
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        # If it's the 1st/3rd/5th/7th rep
        if reps % 8 == 0:
            Message='Pomodoro Alert!!!! Please take a break for {} Minutes Right now!!!'.format(LONG_BREAK_MIN)
            Notify(Message)
            count_down(long_break_sec)
            title_label.config(text="Break", fg=RED)
        # If it's the 8th rep
        elif reps % 2 == 0:
            Message='Pomodoro Alert!!!! Please take a break for {} Minutes Right now!!!'.format(SHORT_BREAK_MIN)
            Notify(Message)
            count_down(short_break_sec)
            title_label.config(text="Break", fg=PINK)
        # If it's the 2nd/4th/6th rep
        else:
            Message='Pomodoro Alert!!!! Work Period Begins for next {} Minutes !!'.format(WORK_MIN)
            Notify(Message)
            count_down(work_sec)
            title_label.config(text="Work", fg=GREEN)
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Dynamic typing allows for changing the data type of a variable
    # Just by assigning it to a different kind of value
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        notification.notify(
        title = "Pomodoro Alert!!!!!",
        message  = " Time up !!!!!!",
        app_icon = None, #image that appears next to tite and message
        timeout = 10)

        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
# Need to check the background colour of the canvas as well
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# highlightthicknes is used for making the highlight disappear
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# count_down(5)
# x and y values are half of the width and the height
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command = reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✓", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
