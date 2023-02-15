import tkinter as tk
window = tk.Tk()
import tkinter.messagebox as tkmb
import random
window.title("Guess the number")
window.geometry("400x400")
window.resizable(False, False)

attemp = 10

secret_number = random.randint(1, 100)
print(secret_number)


def new_game():
    global attemp, secret_number
    attemp = 10
    secret_number = random.randint(1, 100)
    print(secret_number)
    tries["text"] = f"You have: {attemp} tries"
    text["text"] = "Guess the number from 1 to 100"


def check_number():
    global attemp
    number = answer.get()
    if secret_number == int(number):
        text["text"] = "You are guessed the number"
        tkmb.showinfo(title="winner", message="You are guessed the number")
    if secret_number < int(number):
        text["text"] = "Number is smaller than this"
        attemp = attemp -1
        tries["text"] = f"You have: {attemp} tries"
    if secret_number > int(number):
        attemp = attemp - 1
        tries["text"] = f"You have: {attemp} tries"
        text["text"] = "Number is bigger than this"
    answer.delete(0, "end")



text = tk.Label(window, text = "Guess the number from 1 to 100", font = ("Arial", 15))
text.place(x = 85, y = 55)

tries = tk.Label(window, text = f"You have: {attemp} tries", font= ("Arial", 15))
tries.place(x = 85, y = 85)

answer = tk.Entry(window, font = ("Arial"))
answer.place(x = 85, y = 120)

check_btn = tk.Button(window, text = "Check the number", font= ("Arial", 15), command= check_number, background="aquamarine1", fg = "DarkBlue")
check_btn.place(x = 85, y = 150)

new_btn = tk.Button(window, text = "New game", font = ("Arial", 15), command = new_game, background="aquamarine1", fg = "DarkBlue")
new_btn.place(x = 85, y = 200)







window.mainloop()