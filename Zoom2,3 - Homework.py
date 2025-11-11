import tkinter
import random

screen = tkinter.Tk()
screen.geometry("370x200")

player_score = 0
computer_score = 0

def choose_weapon(item):
    global player_score
    global computer_score

    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "rock"
    if comp_choice == 2:
        comp_choice = "paper"
    if comp_choice == 3:
        comp_choice = "scissors"

    urselection.config(text=f"You selected: {item}")
    computerselection.config(text=f"Computer selected: {comp_choice}")

    if item == "rock" and comp_choice == "scissors" or item == "paper" and comp_choice == "rock" or item == "scissors" and comp_choice == "paper":
        player_score += 1
        result_label_two.config(text="Player Won!")

    elif item == comp_choice:
        result_label_two.config(text="Draw!")
    else:
        computer_score += 1
        result_label_two.config(text="Computer Won!")
    playerscore.config(text=f"Player Score: {player_score}")
    computerscore.config(text=f"Computer Score: {computer_score}")


title = tkinter.Label(screen, text="Rock Paper Scissors", bg="lightblue", font="Arial 30 normal")
uroptions = tkinter.Label(screen, text="Your Options:")
r_button = tkinter.Button(screen, text="Rock", bg="red", command=lambda: choose_weapon("rock"))  # Lambda helps make one lined function, stored as a variable.
p_button = tkinter.Button(screen, text="Paper", bg="orange", command=lambda: choose_weapon("paper"))
s_button = tkinter.Button(screen, text="Scissors", bg="green", command=lambda: choose_weapon("scissors"))

result_label_one = tkinter.Label(screen, text="Score:")
result_label_two = tkinter.Label(screen, text="Won!!!")

urselection = tkinter.Label(screen, text="You selected: ")
computerselection = tkinter.Label(screen, text="Computer selected: ")
playerscore = tkinter.Label(screen, text="Player Score: ")
computerscore = tkinter.Label(screen, text="Computer Score: ")

title.grid(row=0, column=0, columnspan=4)
result_label_two.grid(row=1, column=0, columnspan=4)
uroptions.grid(row=2, column=0)
r_button.grid(row=3, column=1, )
p_button.grid(row=3, column=2)
s_button.grid(row=3, column=3)
result_label_one.grid(row=4, column=0)
urselection.grid(row=5, column=1)
computerselection.grid(row=6, column=1)
playerscore.grid(row=5, column=2)
computerscore.grid(row=6, column=2)


screen.mainloop()
