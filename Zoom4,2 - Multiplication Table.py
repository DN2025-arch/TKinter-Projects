import tkinter
import tkinter.ttk  # Sub-module

screen = tkinter.Tk()
screen.geometry("600x600")


def generate_math():
    string_variable = ""

    number = int(number_box.get())
    number_range = int(range_box_var.get())  # get value of selected radiobutton

    for i in range(number_range+1):
        string_variable += f"{number} x {i} = {number*i}\n"

    multiplication_result.config(text=string_variable)


range_box_var = tkinter.IntVar()


title = tkinter.Label(screen, text="Mathematical Table")
txt_1 = tkinter.Label(screen, text="Number and Range:")
number_box = tkinter.ttk.Combobox(screen, )  # Only select one of many hidden options.
range_box_1 = tkinter.Radiobutton(screen, text="10", variable=range_box_var, value=10)  # Only select one of shown options.
range_box_2 = tkinter.Radiobutton(screen, text="20", variable=range_box_var, value=20)  # variable property makes the radiobuttons connected.
range_box_3 = tkinter.Radiobutton(screen, text="30", variable=range_box_var, value=30)  # value property gives the output when selected.
generate_btn = tkinter.Button(screen, text="Generate", command=generate_math)
multiplication_result = tkinter.Label(screen)


number_box_list = [i for i in range(1, 100+1)]  # Always have list (going to Combo_box) after Combo_Box
number_box["values"] = number_box_list  # Manually Add list to Combo_box's values.


title.grid(row=0, column=0, columnspan=3)
txt_1.grid(row=1, column=0)
number_box.grid(row=1, column=1)
range_box_1.grid(row=1, column=2)
range_box_2.grid(row=2, column=2)
range_box_3.grid(row=3, column=2)
generate_btn.grid(row=4, column=1)
multiplication_result.grid(row=5, column=1)

screen.mainloop()
