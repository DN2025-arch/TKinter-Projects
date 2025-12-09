import tkinter
import random
import time

global_color = "white"

p1_score = 0
p2_score = 0

screen = tkinter.Tk()
screen.geometry("1000x600")

cnvs = tkinter.Canvas(screen, bg="black", width=1000, height=600)

scoreboard = cnvs.create_text(50, 50, text=f"{p1_score}:{p2_score}", fill="white", font="arial 30 normal")

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
    global p1_score
    global p2_score

    cnvs.move(ball, vx, vy)  # Object, Velocity of X, Velocity of Y.

    coordinates = cnvs.coords(ball)  # Gets coords of shape, form of tuple: x1,y1, x2,y2
    if coordinates[0] <= 0:     # x1
        vx = abs(vx)
        p2_score += 1
    if coordinates[1] >= 600:  #y1
        vy = abs(vy) * -1
    if coordinates[2] >= 1000:  #x2
        vx = abs(vx) * -1
        p1_score += 1
    if coordinates[3] <= 0:     #y2
        vy = abs(vy)

    p1_coords = cnvs.coords(p1)
    p2_coords = cnvs.coords(p2)

    if coordinates[1] <= p1_coords[3] and coordinates[3] >= p1_coords[1]:
        if coordinates[0] <= p1_coords[2] and coordinates[0] >= p1_coords[0]:
            vx = abs(vx)

    if coordinates[1] <= p2_coords[3] and coordinates[3] >= p2_coords[1]:
        if coordinates[2] >= p2_coords[0] and coordinates[2] >= p2_coords[2]:
            vx = abs(vx) * -1

    cnvs.itemconfigure(scoreboard, text=f"{p1_score}:{p2_score}")
    
    #print(f"{p1_score}:{p2_score}")


p1_speed = 0
p2_speed = 0
def move_p1(p1_speed):
    cnvs.move(p1, 0, p1_speed)
def move_p2(p2_speed):
    cnvs.move(p2, 0, p2_speed)

def key_w(event):
    global p1_speed
    p1_speed = -5
def key_s(event):
    global p1_speed
    p1_speed = 5

def key_up(event):
    global p2_speed
    p2_speed = -5
def key_down(event):
    global p2_speed
    p2_speed = 5

screen.bind("<w>", key_w)
screen.bind("<s>", key_s)
screen.bind("<KeyPress-Up>", key_up)
screen.bind("<KeyPress-Down>", key_down)

cnvs.pack()

def game_loop():
    global p1_speed
    global p2_speed
    move_ball()
    move_p1(p1_speed)
    move_p2(p2_speed)
    
    screen.update()  # Update frames/screen
    screen.update_idletasks()

    screen.after(10, game_loop)  # Calls function after 10 miliseconds.
    
game_loop()
screen.mainloop()
