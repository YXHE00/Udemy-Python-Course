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
CHECKMARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
# reset the timer and cancel it
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # call the function and the counts down show in the screen
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# after takes an amount of time that it should wait and after that calls a particular function
def count_down(count):
    # format the time
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Dynamic typing - change a variable data type by changing the content in that variable
    if count_sec < 10:  # data type: int
        count_sec = f"0{count_sec}"  # data type: str

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()  # when finished count down, repeat start_timer(), reps + 1
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += CHECKMARK
        checkmark_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)  # set the padding and background color

# add Timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)  # fg stands for foreground
timer_label.grid(column=1, row=0)


# add tomato image to the window
# highlightthickness remove the frame, make sure the background color keep the same
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # 100, 112 make the image at middle


# timer shows on the screen
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)


# reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


# check mark ✔
checkmark_label = Label(fg=GREEN, bg=YELLOW)  # start with empty
checkmark_label.grid(column=1, row=3)


window.mainloop()
