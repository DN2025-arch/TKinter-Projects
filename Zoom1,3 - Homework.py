import tkinter

screen = tkinter.Tk()
screen.geometry("370x70")

l1 = tkinter.Label(screen, text="Enter the Weight in Kg")
e1 = tkinter.Entry(screen)
b1 = tkinter.Button(screen, text="Convert")
l2 = tkinter.Label(screen, text="Grams")
l3 = tkinter.Label(screen, text="Pounds")
l4 = tkinter.Label(screen, text="Ounces")
e2 = tkinter.Label(screen)
e3 = tkinter.Label(screen)
e4 = tkinter.Label(screen)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
b1.grid(row=0, column=2)
l2.grid(row=1, column=0)
l3.grid(row=1, column=1)
l4.grid(row=1, column=2)
e2.grid(row=2, column=0)
e3.grid(row=2, column=1)
e4.grid(row=2, column=2)

screen.mainloop()
