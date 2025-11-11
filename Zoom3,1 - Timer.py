import tkinter
import tkinter.messagebox  # Used for showing specific windows with specific purposes
import time

screen = tkinter.Tk()
screen.geometry("400x400")

hour = tkinter.StringVar()
minute = tkinter.StringVar()
second = tkinter.StringVar()

hour.set("00")  # Set string
minute.set("00")
second.set("00")


def start_timer():
    t_hours = int(hours.get())
    t_minutes = int(minutes.get())
    t_seconds = int(seconds.get())

    total_seconds = t_seconds + (t_minutes*60) + (t_hours*3600)

    while total_seconds > 0:

        time.sleep(1)
        t_seconds -= 1
        if t_seconds < 0:
            t_minutes -= 1
            t_seconds = 59
        if t_minutes < 0:
            t_hours -= 1
            t_minutes = 59
        total_seconds -= 1

        hour.set("{:002d}".format(t_hours))
        minute.set("{:002d}".format(t_minutes))
        second.set("{:002d}".format(t_seconds))

        if t_hours == 0 and t_minutes == 0 and t_seconds == 0:
            tkinter.messagebox.askokcancel("Time Unit Error", "Time Units Reached Zero")

        screen.update()  # Refresh Screen


hours = tkinter.Entry(screen, textvariable=hour)
minutes = tkinter.Entry(screen, textvariable=minute)
seconds = tkinter.Entry(screen, textvariable=second)

set_timer = tkinter.Button(screen, text="Set Time Cooldown", command=start_timer)

hours.grid(row=0, column=0)
minutes.grid(row=0, column=1)
seconds.grid(row=0, column=2)

set_timer.grid(row=1, column=0, columnspan=3)

screen.mainloop()
