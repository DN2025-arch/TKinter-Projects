import tkinter
import tkinter.messagebox
import random

screen = tkinter.Tk()
screen.geometry("230x230")


def check_winner():
    for i in winning_combinations:
        if i[0]["text"] == "X" and i[1]["text"] == "X" and i[2]["text"] == "X":
            turn_indicator.config(text="Player 1 Wins")
            list_of_buttons.clear()
            tkinter.messagebox.showinfo("Game Result", "Player 1 Won!")
        if i[0]["text"] == "O" and i[1]["text"] == "O" and i[2]["text"] == "O":
            turn_indicator.config(text="Player 2 Wins")
            list_of_buttons.clear()
            tkinter.messagebox.showinfo("Game Result", "Player 2 Won!")


turn = 1
def place(button):
    global turn
    if button in list_of_buttons:
        if turn == 1:
            turn_indicator.config(text="Player 2 Turn")
            button.config(text="X")
            turn = 2
        else:
            turn_indicator.config(text="Player 1 Turn")
            button.config(text="O")
            turn = 1
        list_of_buttons.remove(button)
        check_winner()
        if not list_of_buttons and turn_indicator["text"] == "Player 2 Turn":
            turn_indicator.config(text="Draw!")
            tkinter.messagebox.showwarning("Game Result", "Draw!")


button_width = 8  # Uses character length
button_height = 3
button_padding_x = 5
button_padding_y = 5


button1 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button1))
button2 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button2))
button3 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button3))
button4 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button4))
button5 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button5))
button6 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button6))
button7 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button7))
button8 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button8))
button9 = tkinter.Button(screen, text="", width=button_width, height=button_height, command=lambda: place(button9))
turn_indicator = tkinter.Label(screen, text="Player 1 Turn")

list_of_buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

winning_combinations = [
    [button1, button2, button3],
    [button1, button4, button7],
    [button1, button5, button9],
    [button2, button5, button8],
    [button3, button6, button9],
    [button3, button5, button7],
    [button4, button5, button6],
    [button7, button8, button9],

]

button1.grid(row=0, column=0, padx=button_padding_x, pady=button_padding_y)
button2.grid(row=0, column=1, padx=button_padding_x, pady=button_padding_y)
button3.grid(row=0, column=2, padx=button_padding_x, pady=button_padding_y)
button4.grid(row=1, column=0, padx=button_padding_x, pady=button_padding_y)
button5.grid(row=1, column=1, padx=button_padding_x, pady=button_padding_y)
button6.grid(row=1, column=2, padx=button_padding_x, pady=button_padding_y)
button7.grid(row=2, column=0, padx=button_padding_x, pady=button_padding_y)
button8.grid(row=2, column=1, padx=button_padding_x, pady=button_padding_y)
button9.grid(row=2, column=2, padx=button_padding_x, pady=button_padding_y)
turn_indicator.grid(row=3, column=1)

screen.mainloop()
