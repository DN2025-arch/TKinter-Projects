import tkinter.ttk

screen = tkinter.Tk()
screen.geometry("600x270")


def order():
    pizza_type = ""
    pizza_quantity = ""
    pizza_size = ""
    pizza_type = pizza_selection_combobox.get()
    pizza_quantity = quantity_combobox.get()
    pizza_size = range_box_var.get()
    result["text"] = f"You ordered {pizza_quantity} {pizza_type} {pizza_size} Pizza(s)"
    if pizza_type == "" or pizza_quantity == "" or pizza_size == "":
        result["text"] = "Please Select All Options"


range_box_var = tkinter.StringVar()

title = tkinter.Label(screen, text="Welcome to Pizza Hut")
pizza_selection_label = tkinter.Label(screen, text="Select Your Fav Pizza:")
pizza_selection_combobox = tkinter.ttk.Combobox(screen)
quantity_label = tkinter.Label(screen, text="Enter Quantity:")
quantity_combobox = tkinter.ttk.Combobox(screen)
size_radiobutton1 = tkinter.Radiobutton(screen, text="S", variable=range_box_var, value="Small")
size_radiobutton2 = tkinter.Radiobutton(screen, text="M", variable=range_box_var, value="Medium")
size_radiobutton3 = tkinter.Radiobutton(screen, text="L", variable=range_box_var, value="Large")
order_button = tkinter.Button(screen, text="Order", command=order)
result = tkinter.Label(screen, text="")

pizza_selection_options = ["Veg Extravaganza", "Margarita", "Pepperoni", "Meatball Surprise"]
pizza_selection_combobox["values"] = pizza_selection_options

quantity_options = [i for i in range(1, 10+1)]
quantity_combobox["values"] = quantity_options


default_padx = 10
default_pady = 3

title.grid(row=0, column=0, columnspan=3, padx=default_padx, pady=default_pady)
pizza_selection_label.grid(row=1, column=0, padx=default_padx, pady=default_pady)
pizza_selection_combobox.grid(row=1, column=1, padx=default_padx, pady=default_pady)
quantity_label.grid(row=2, column=0, padx=default_padx, pady=default_pady)
quantity_combobox.grid(row=2, column=1, padx=default_padx, pady=default_pady)
size_radiobutton1.grid(row=1, column=2, padx=default_padx, pady=default_pady)
size_radiobutton2.grid(row=2, column=2, padx=default_padx, pady=default_pady)
size_radiobutton3.grid(row=3, column=2, padx=default_padx, pady=default_pady)
order_button.grid(row=3, column=1, padx=default_padx, pady=default_pady)
result.grid(row=4, column=0, columnspan=3, padx=default_padx, pady=default_pady)


screen.mainloop()
