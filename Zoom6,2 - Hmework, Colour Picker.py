import tkinter

screen = tkinter.Tk()
screen.geometry("400x400")

def select():
    selected_color = color_list.selection_get()  ##Value Selection
    print(selected_color)
    screen.config(bg=selected_color)

def add():
    adding_color = add_color_entry.get()
    if adding_color == "":
        return
    color_list.insert(tkinter.END, adding_color)
    add_color_entry.delete(0, tkinter.END)

def delete():
    selected_color = color_list.curselection()  ##Index Selection
    color_list.delete(selected_color)

select_color = tkinter.Button(screen, text="Select", command=select)
add_color_entry = tkinter.Entry(screen)
add_color = tkinter.Button(screen, text="+", command=add)
delete_color = tkinter.Button(screen, text="x", command=delete)

color_list = tkinter.Listbox(screen, width=40)

colors = ["red",
          "blue",
          "green",
          "black",
          "white"]

for color in colors:
    color_list.insert(tkinter.END, color)

def_padx = 5
def_pady = 5

select_color.grid(row=0, column=0, padx=def_padx, pady=def_pady)
delete_color.grid(row=0, column=1, padx=def_padx, pady=def_pady)
add_color_entry.grid(row=0, column=2, padx=def_padx, pady=def_pady)
add_color.grid(row=0, column=3, padx=def_padx, pady=def_pady)
color_list.grid(row=1, column=0, columnspan=4, padx=def_padx, pady=def_pady)

screen.mainloop()
