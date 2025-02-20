import tkinter as tk
import random

win = tk.Tk()
win.grid_rowconfigure(1, minsize=70)  # Empty row
win.grid_columnconfigure(1, minsize=400)  # Empty column
win.grid_rowconfigure(3, minsize=20)  # Empty row
win.grid_columnconfigure(3, minsize=80)
win.grid_rowconfigure(5, minsize=20)  # Empty row
win.grid_columnconfigure(5, minsize=20)
win.grid_rowconfigure(7, minsize=20)  # Empty row
win.grid_columnconfigure(7, minsize=20)
win.grid_rowconfigure(9, minsize=20)  # Empty row
win.grid_columnconfigure(9, minsize=20)

title = tk.Label(win, text="WORDLE", fg="purple", font=("ALGERIAN", 40))
title.grid(row=1, column=6)

# Create StringVar list for button texts (5 rows, 4 columns)
button_vars = [[tk.StringVar(value="") for _ in range(4)] for _ in range(5)]
buttons = []
positions = [
    (2, 2), (2, 4), (2, 6), (2, 8),
    (4, 2), (4, 4), (4, 6), (4, 8),
    (6, 2), (6, 4), (6, 6), (6, 8),
    (8, 2), (8, 4), (8, 6), (8, 8),
    (10, 2), (10, 4), (10, 6), (10, 8),
]

# Create and place the buttons
for i in range(5):
    row_buttons = []
    for j in range(4):
        button = tk.Button(win, textvariable=button_vars[i][j],
                           width=7, height=3, bg="gray", fg="white", font=("Arial", 20))
        button.grid(row=positions[i * 4 + j][0], column=positions[i * 4 + j][1])
        row_buttons.append(button)
    buttons.append(row_buttons)


wordles = ["hell","very","fart","hymn","bevy","bird","tear"]
wordle=random.choice(wordles)
current_attempt = 0  # Global counter for attempts

def update_button_text():
    global current_attempt
    user_text = entry.get().strip()  # Get user input and remove whitespace

    # Ensure the input is exactly 4 characters
    if len(user_text) != 4:
        print("Please enter exactly 4 characters")
        return

    user_string = list(user_text)

    # Update the corresponding row's buttons based on the current attempt
    for j in range(4):
        button_vars[current_attempt][j].set(user_string[j])
        if user_string[j] == wordle[j]:
            buttons[current_attempt][j].config(bg="green")
        elif user_string[j] in wordle:
            buttons[current_attempt][j].config(bg="#e8e109")  # Yellow color
        else:
            buttons[current_attempt][j].config(bg="gray")  # Remain gray if not present

    current_attempt += 1  # Move to the next attempt/row
    entry.delete(0, tk.END)  # Clear the input field

    # If 5 attempts have been used, disable further input
    if current_attempt >= 5:
        submit_btn.config(state="disabled")
        entry.config(state="disabled")
        print("No more attempts left!")

# Input field and submit button
entry = tk.Entry(win, font=("Arial", 20))
entry.grid(row=12, column=2, columnspan=3)

submit_btn = tk.Button(win, text="Submit", command=update_button_text, font=("Arial", 20))
submit_btn.grid(row=12, column=6)

win.mainloop()
