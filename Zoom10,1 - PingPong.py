import tkinter
import random
import time

global_color = "white"

screen = tkinter.Tk()
screen.geometry("1000x600")

cnvs = tkinter.Canvas(screen, bg="black", width=1000, height=600)

# Draw Background
cnvs.create_line(500, 600, 500, 0, fill=global_color, width=10)
cnvs.create_oval(400, 400, 600, 200, outline=global_color, width=10)  # Create any shape, from top corner to bottom.

ball = cnvs.create_oval(40, 290, 60, 310, fill=global_color)
p1 = cnvs.create_rectangle(30, 250, 40, 350, fill=global_color)  # FIRST value smaller
p2 = cnvs.create_rectangle(960, 250, 970, 350, fill=global_color)

vx = 10                      # Velocity of x.
vy = random.randint(-10,10)  # Velocity of y.
vy = 5

def move_ball():
    global vx
    global vy

    cnvs.move(ball, vx, vy)  # Object, Velocity of X, Velocity of Y.

    coordinates = cnvs.coords(ball)  # Gets coords of shape, form of tuple: x1,y1, x2,y2
    if coordinates[0] <= 0:     # x1
        vx = abs(vx)
    if coordinates[1] >= 600:  #y1
        vy = vy * -1
    if coordinates[2] >= 1000:  #x2
        vx = vx * -1
    if coordinates[3] <= 0:     #y2
        vy = abs(vy)

p1vy = 0
p2vy = 0
def move_p1():
    cnvs.move(p1, 0, p1vy)
    print(p1vy)
def move_p2():
    cnvs.move(p2, 0,p2vy)

def key_w(event):
    global p1_vy
    p1_vy = 10
def key_s(event):
    global p1_vy
    p1_vy = -10

screen.bind("<w>", key_w)
screen.bind("<s>", key_s)

cnvs.pack()

def game_loop():
    move_ball()
    move_p1()
    move_p2()

    screen.update()  # Update frames/screen
    screen.update_idletasks()

    screen.after(10, game_loop)  # Calls function after 10 miliseconds.
    
game_loop()
screen.mainloop()
