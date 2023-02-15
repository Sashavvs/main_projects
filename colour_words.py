import tkinter as tk
window = tk.Tk()
import random
window.title("Guess the colour")
window.geometry("400x400")
window.resizable(False, False)

time = 30

correct = 0
incorrect = 0


colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown"]

def new_game():
    global time, correct, incorrect
    time = 30
    correct = 0
    incorrect = 0
    correct_label["text"] = f"Correct answers: {correct}"
    incorrect_label["text"] = f"Incorrect answers: {incorrect}"
    time_label["text"] = f"Starting a new game: {time}"
    time_label.after(1000, timer)


def timer():
    global time
    if time > 0:
        time = time - 1
        time_label["text"] = f"Time left: {time}"
        time_label.after(1000, timer)
    print(time)


def new_word ():
    colour_text ["text"] = random.choice(colors)
    colour_text["fg"] = random.choice(colors)


def check (event):
    print("function is working")
    global correct, incorrect, time
    if time > 0:
        user_color = answer.get()
        correct_color = colour_text["fg"]
        if user_color == correct_color:
            correct = correct + 1
            correct_label["text"] = f"Correct answers: {correct}"
            print(correct)
        else:
            incorrect = incorrect + 1
            incorrect_label["text"] = f"Incorrect answers: {incorrect}"
            print(incorrect)
        new_word()

        answer.delete(0, "end")
    if time == 0:
        new_game()


window.bind("<Return>", check)

new_g = tk.Button(window, text = "New game", font = ("Arial", 15), command= new_game)
new_g.place(x = 85, y = 275)

correct_label = tk.Label(window, text = f"Correct answers: {correct}", font = ("Arial", 15))
correct_label.place(x = 85, y = 55)

incorrect_label = tk.Label(window, text = f"Incorrect answers: {incorrect}", font = ("Arial", 15))
incorrect_label.place(x = 85, y = 85)

instructions = tk.Label(window, text = "Enter the words colour", font = ("Arial", 15))
instructions.place(x = 85, y = 25)

colour_text = tk.Label(window, text = "colour", font = ("Arial", 40))
colour_text.place(x = 90, y = 125)

answer = tk.Entry(window, font = ("Arial", 15))
answer.place(x = 90, y = 190)

time_label = tk.Label(window, text = f"Time left: {time}", font = ("Arial", 15))
time_label.place(x = 85, y = 235)

timer()

answer.focus_set()

new_word()




window.mainloop()