#  Calender Project

import tkinter
import calendar


def show_year():
    year = int(e_enter_year.get())
    cal = calendar.calendar(year)
    print(year)
    screen_cal = tkinter.Tk()
    screen_cal.geometry("600x600")

    l_calendar = tkinter.Text(screen_cal, height=36)  # Text is for strings on multiple lines.
    # Height increases how many lines there are in a text: Number of lines.
    l_calendar.insert(tkinter.END, cal)  # Text must have the strings inserted, ideally.
    # Must have an index value first, tkinter.END inserts text at the last index.

    l_calendar.pack()

    screen_cal.mainloop()


screen = tkinter.Tk()
screen.geometry("400x400")

# font="font 30 *" *= normal/bold/italic
# bg=color (background)
# fg=color (foreground)

# command=function  NO BRACKETS

# default font, Segoe
l_title = tkinter.Label(screen, text="Calender", font="Arial 30 normal", bg="gray", fg="white")
l_button_desc = tkinter.Label(screen, text="Enter Year:")
e_enter_year = tkinter.Entry(screen)
b_show_calender = tkinter.Button(screen, text="Show Calender", command=show_year)
b_exit = tkinter.Button(screen, text="Exit")

l_title.pack()
l_button_desc.pack()
e_enter_year.pack()
b_show_calender.pack()
b_exit.pack()

screen.mainloop()

# Compiler takes whole code, and convert it to a machine-understandable code, then execute it. ()
# Interpreter takes one line, convert it to a machine-understandable code, then execute it.    (Python)
