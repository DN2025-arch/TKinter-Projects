import tkinter as tk
from tkinter.colorchooser import askcolor

screen = tk.Tk()
screen.geometry("700x700")

pensize = 10
pencolor = "blue"
pen_on = True
old_x = None
old_y = None
def setup():
    print("")


def draw(event):
    global pensize
    global pencolor
    global pen_on
    global old_x
    global old_y
    pensize = slider.get()
    
    if pen_on:
        drawingcolor = pencolor
    else:
        drawingcolor = "white"

    if old_x and old_y:
        cnvs.create_line(old_x, old_y, event.x, event.y, width=pensize, fill=drawingcolor, capstyle=tk.ROUND)
    old_x = event.x
    old_y = event.y

def reset(event):
    global old_x
    global old_y
    old_x = None
    old_y = None

    
def pen():
    global pen_on
    pen_on = True
    activate(btn_pen)

    
def activate(button):
    global active_btn

    active_btn.config(relief=tk.RAISED)
    
    button.config(relief=tk.SUNKEN)
    active_btn = button
    
def color():
    global pencolor
    pencolor = askcolor()[1]

    
def eraser():
    global pen_on
    pen_on = False
    activate(btn_eraser)
    

btn_pen = tk.Button(screen, text="PEN", command=pen)
btn_brush = tk.Button(screen, text="BRUSH", command=activate)
btn_color = tk.Button(screen, text="COLOR", command=color)
btn_eraser = tk.Button(screen, text="ERASER", command=eraser)
slider = tk.Scale(screen, from_=1, to=10, orient=tk.HORIZONTAL)
cnvs = tk.Canvas(screen, bg="white", width=600, height=600)

active_btn = btn_pen

cnvs.bind("<B1-Motion>", draw)
cnvs.bind("<ButtonRelease-1>", reset)

btn_pen.grid(row=0, column=0)
btn_brush.grid(row=0, column=1)
btn_color.grid(row=0, column=2)
btn_eraser.grid(row=0, column=3)
slider.grid(row=0, column=4)

cnvs.grid(row=2, column=0, columnspan=5)

screen.mainloop()
