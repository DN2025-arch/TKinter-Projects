import tkinter
import tkinter.messagebox
import tkinter.filedialog

color_1 = "#F27C73"
color_2 = "#D75C53"
color_3 = "#F88F6E"

student_details = {
    "John": ["65675", "60", "40", "83%"],
    "Jimmy": ["65788", "30", "55", "71%"],
    "Jan": ["65796", "12", "8", "17%"]
    }

screen = tkinter.Tk()
screen.geometry("600x400")
screen.config(bg=color_1)


def update_listbox():
    student_listbox.delete(0, tkinter.END)
    for student in student_details.keys():
        student_listbox.insert(tkinter.END, student)


def clear_entries():
    name_E.delete(0, tkinter.END)
    num_E.delete(0, tkinter.END)
    sci_E.delete(0, tkinter.END)
    mth_E.delete(0, tkinter.END)
    prc_E.delete(0, tkinter.END)


def update():
    name = name_E.get()
    num = num_E.get()
    sci = sci_E.get()
    mth = mth_E.get()
    prc = prc_E.get()

    student_details[name] = [num, sci, mth, prc]

    clear_entries()
    update_listbox()


def delete():
    curstudent = student_listbox.selection_get()
    del student_details[curstudent]

    update_listbox()


def edit(event):
    clear_entries()
    curstudent = student_listbox.selection_get()

    name_E.insert(tkinter.END, curstudent)
    num_E.insert(tkinter.END, student_details[curstudent][0])
    sci_E.insert(tkinter.END, student_details[curstudent][1])
    mth_E.insert(tkinter.END, student_details[curstudent][2])
    prc_E.insert(tkinter.END, student_details[curstudent][3])


def show():
    curstudent = student_listbox.selection_get()

    num = student_details[curstudent][0]
    sci = student_details[curstudent][1]
    mth = student_details[curstudent][2]
    prc = student_details[curstudent][3]

    tkinter.messagebox.showinfo("Score Summary", f"Student {num}: {curstudent} has a score of {sci} on their latest science test and {mth} on their latest maths test, averaging to {prc}.")


def save():
    students_file = tkinter.filedialog.asksaveasfile()
    if students_file is not None:
        print(student_details, file=students_file)


def load():
    global student_details
    students_file = tkinter.filedialog.askopenfile()
    if students_file is not None:
        content = students_file.readline()
        student_details = eval(content)
    update_listbox()



title = tkinter.Label(screen, text="STUDENT INFORMATION AND MARKS LOGGER", bg=color_2)
subtitle = tkinter.Label(screen, text="STUDENT REPORT LOG", bg=color_2)

name_L = tkinter.Label(screen, text="Name:", bg=color_3)
num_L = tkinter.Label(screen, text="Roll/Number:", bg=color_3)
sci_L = tkinter.Label(screen, text="Science Marks:", bg=color_3)
mth_L = tkinter.Label(screen, text="Maths Marks:", bg=color_3)
prc_L = tkinter.Label(screen, text="Percentage:", bg=color_3)

name_E = tkinter.Entry(screen, bg=color_2)
num_E = tkinter.Entry(screen, bg=color_2)
sci_E = tkinter.Entry(screen, bg=color_2)
mth_E = tkinter.Entry(screen, bg=color_2)
prc_E = tkinter.Entry(screen, bg=color_2)

student_listbox = tkinter.Listbox(screen, width=80, bg=color_2)
update_listbox()

student_listbox.bind("<<ListboxSelect>>", edit)

bottom_button_width = 10
show_btn = tkinter.Button(screen, text="Show", width=bottom_button_width, bg=color_3, command=show)
del_btn = tkinter.Button(screen, text="Delete", width=bottom_button_width, bg=color_3, command=delete)
open_btn = tkinter.Button(screen, text="Open", width=bottom_button_width, bg=color_3, command=load)
upd_btn = tkinter.Button(screen, text="Update/Add", width=bottom_button_width, bg=color_3, command=update)
save_btn = tkinter.Button(screen, text="Save", width=bottom_button_width, bg=color_3, command=save)



px = 5
py = 5

title.grid(row=0, column=0, columnspan=5, padx=px, pady=py)
subtitle.grid(row=1, column=0, padx=px, pady=py)

name_L.grid(row=2, column=0, padx=px, pady=py)
name_E.grid(row=2, column=1, padx=px, pady=py)
num_L.grid(row=3, column=0, padx=px, pady=py)
num_E.grid(row=3, column=1, padx=px, pady=py)
sci_L.grid(row=2, column=3, padx=px, pady=py)
sci_E.grid(row=2, column=4, padx=px, pady=py)
mth_L.grid(row=3, column=3, padx=px, pady=py)
mth_E.grid(row=3, column=4, padx=px, pady=py)
prc_L.grid(row=4, column=3, padx=px, pady=py)
prc_E.grid(row=4, column=4, padx=px, pady=py)

student_listbox.grid(row=5, columnspan=5, padx=px, pady=py)

show_btn.grid(row=6, column=0, padx=px, pady=py)
del_btn.grid(row=6, column=1, padx=px, pady=py)
open_btn.grid(row=6, column=2, padx=px, pady=py)
upd_btn.grid(row=6, column=3, padx=px, pady=py)
save_btn.grid(row=6, column=4, padx=px, pady=py)

screen.mainloop()
