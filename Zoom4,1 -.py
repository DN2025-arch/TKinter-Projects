import tkinter
import tkinter.messagebox
import random

screen = tkinter.Tk()
screen.geometry("400x400")

defult_attempts = 2
attempts = defult_attempts
random_number = -1
player_name = ""


def begin():
    global player_name
    global random_number
    global attempts
    player_name = name_input.get()

    tkinter.messagebox.askokcancel("name", f"Well, {player_name}, I am thinking of a number between 1 and 20.")

    # Begin/Restart Game
    attempts = defult_attempts
    random_number = random.randint(1, 20)


def show_attempts():
    global attempts
    attempts -= 1
    if attempts > 0:
        tkinter.messagebox.showwarning("Uh oh", f"You have {attempts} attempts left!")
    else:
        tkinter.messagebox.showwarning("Uh oh", "You ran out of tries!")


def guess_number():
    global player_name
    global random_number
    global attempts

    if attempts > 0:
        player_guess = int(guess_input.get())

        if player_guess == random_number:
            tkinter.messagebox.showinfo("Info", f"Well done {player_name}, You got it right!")
        elif player_guess > random_number:
            tkinter.messagebox.showinfo("Info", "Incorrect, Your number is higher than my number!")
            show_attempts()
        elif player_guess < random_number:
            tkinter.messagebox.showinfo("Info", "Incorrect, Your number is lower than my number!")
            show_attempts()
        else:
            tkinter.messagebox.showinfo("Info", "Incorrect, try again!")


title = tkinter.Label(screen, text="Welcome to our game!")
name_detail = tkinter.Label(screen, text="What's your Name?")
name_input = tkinter.Entry(screen)
name_accept_btn = tkinter.Button(screen, text="OK", command=begin)
guess_detail = tkinter.Label(screen, text="Take a Guess:")
guess_input = tkinter.Entry(screen)
guess_accept_btn = tkinter.Button(screen, text="Guess", command=guess_number)

var_padx = 10

title.grid(row=0, column=0, columnspan=2, pady=25, padx=var_padx)
name_detail.grid(row=1, column=0, pady=5, padx=var_padx)
name_input.grid(row=2, column=0, padx=var_padx)
name_accept_btn.grid(row=2, column=1, padx=var_padx)
guess_detail.grid(row=3, column=0, pady=5, padx=var_padx)
guess_input.grid(row=4, column=0, padx=var_padx)
guess_accept_btn.grid(row=4, column=1, padx=var_padx)

screen.mainloop()
