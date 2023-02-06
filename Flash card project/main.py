from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# print(to_learn)  # [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},.....]
current_card = {}

# set a global variable, which starts out as an empty dictionary
to_learn = {}

# words_to_learn.csv not stored inside file, it creates after click the button to change the word show on the screen
try:
    # use the pandas to read csv file which only contents the unknown cards
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:  # if words_to_learn.csv not exists, use the original file as to_learn list
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    # convert csv to dictionary and use the orient set to the records, this gives each column of values as a list
    to_learn = data.to_dict(orient="records")


# pick up the word from to_learn randomly
def next_card():
    global current_card, flip_timer

    # everytime goto the new card(click the button), we are going to invalidate this timer
    window.after_cancel(flip_timer)

    # randomly change the title and word when click the button
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    # after setup the card, we can setup a new flip_timer, so it waits for again 3 seconds
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    # remove the current card from the cards list (to_learn)
    # after remove, the length of the cards list will reduce one card
    to_learn.remove(current_card)

    # store the unknown data inside a new csv file
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)  # index not add into new created list

    # call nex_card() function to change the current card title and word
    next_card()


# changing the card to show the English word for the current card, and also change the image to the card_back.png
def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# create a window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# after configured everything on the card, then call the 3 seconds flip_card
flip_timer = window.after(3000, func=flip_card)

# add images inside the window, size equal to card image size
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# save the image and give a variable name
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# create image size
card_background = canvas.create_image(400, 263, image=card_front_img)

# texts show on the card
title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create unknown button
unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# create right button
checkmark_img = PhotoImage(file="images/right.png")
known_button = Button(image=checkmark_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# once create everything, then can generate the next_card(), get the card title and word on the screen
next_card()

window.mainloop()


