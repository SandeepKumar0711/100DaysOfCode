from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# reading from file


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    temp = pandas.DataFrame(to_learn)
    temp.to_csv("data/words_to_learn.csv", index=False)
    next_word()


try:
    word_data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    word_data = pandas.read_csv('data/french_words.csv')
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

to_learn = word_data.to_dict(orient="records")
current_card = {}
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

title_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_word()
window.mainloop()
