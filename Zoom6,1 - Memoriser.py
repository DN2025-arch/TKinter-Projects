import tkinter
import random
import tkinter.filedialog  # For tkinter files

screen = tkinter.Tk()
screen.geometry("400x400")


def save():
    memoriser_file = tkinter.filedialog.asksaveasfile()
    if memoriser_file is not None:  # None: empty; If the file was created then..
        content = text_list.get(0, tkinter.END)
        for i in content:
            print(i, file=memoriser_file)  # file=... ,prints x in a file


def open():
    text_list.delete(0, tkinter.END)
    memoriser_file = tkinter.filedialog.askopenfile()
    if memoriser_file is not None:
        content = memoriser_file.readlines()  # Reads each line
        for i in content:  # Gets each line
            text_list.insert(tkinter.END, i)


def delete():
    index_position = text_list.curselection()  # Gets current index selection of list_box
    for i in reversed(index_position):  # reversed() goes from the end
        text_list.delete(i)
    # If we delete from the starting index, all the position of the indexes will shift.


def add():
    if not enter_text.get() == "":
        adding_text = enter_text.get()
        text_list.insert(tkinter.END, adding_text)  # tkinter.END, gives last index position
        enter_text.delete(0, tkinter.END)  # from the first character to the last


default_width = 10

open_btn = tkinter.Button(screen, text="OPEN", width=default_width, command=open)
del_btn = tkinter.Button(screen, text="DELETE", width=default_width, command=delete)
save_btn = tkinter.Button(screen, text="SAVE", width=default_width, command=save)
add_btn = tkinter.Button(screen, text="ADD", width=default_width, command=add)
enter_text = tkinter.Entry(screen, width=30)

text_list = tkinter.Listbox(screen, width=50, selectmode=tkinter.MULTIPLE)  # A big list of text.
# By default you can only select one item at a time. selectmode changes how many u can select (optional)

default_padx = 5
default_pady = 5

open_btn.grid(row=0, column=0, padx=default_padx, pady=default_pady)
del_btn.grid(row=0, column=1, padx=default_padx, pady=default_pady)
save_btn.grid(row=0, column=2, padx=default_padx, pady=default_pady)
enter_text.grid(row=1, column=0, columnspan=2, padx=default_padx, pady=default_pady)
add_btn.grid(row=1, column=2, padx=default_padx, pady=default_pady)
text_list.grid(row=2, column=0, columnspan=3, padx=default_padx, pady=default_pady)

screen.mainloop()
