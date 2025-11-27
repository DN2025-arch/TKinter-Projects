import tkinter
import tkinter.messagebox
import tkinter.filedialog

screen = tkinter.Tk()
screen.geometry("400x400")

contacts = {
"Daniel": ["Maples Avanue", "07784 567886", "Dan_Nis13@Yahoo.com", "9 Sep 2011"],
    }

def update_listbox():
    shown_contacts.delete(0, tkinter.END)
    for name in contacts.keys():
        shown_contacts.insert(tkinter.END, name)


def update():
    cng_name = name_E.get()
    cng_add = add_E.get()
    cng_mob = mob_E.get()
    cng_email = email_E.get()
    cng_birth = birth_E.get()

    contacts[cng_name] = [cng_add, cng_mob, cng_email, cng_birth]

    name_E.delete(0, tkinter.END)
    add_E.delete(0, tkinter.END)
    mob_E.delete(0, tkinter.END)
    email_E.delete(0, tkinter.END)
    birth_E.delete(0, tkinter.END)

    update_listbox()
    print(contacts)


def show():
    curname = shown_contacts.selection_get()

    name = curname
    add = contacts[curname][0]
    mob = contacts[curname][1]
    email = contacts[curname][2]
    birth = contacts[curname][3]
    
    contact_info = f"{name}\n {add}\n {mob}\n {email}\n {birth}"

    tkinter.messagebox.showinfo("Contact Detail", contact_info)


def edit(event):

    name_E.delete(0, tkinter.END)
    add_E.delete(0, tkinter.END)
    mob_E.delete(0, tkinter.END)
    email_E.delete(0, tkinter.END)
    birth_E.delete(0, tkinter.END)
    
    curname = shown_contacts.selection_get()
    name_E.insert(tkinter.END, curname)
    add_E.insert(tkinter.END, contacts[curname][0])
    mob_E.insert(tkinter.END, contacts[curname][1])
    email_E.insert(tkinter.END, contacts[curname][2])
    birth_E.insert(tkinter.END, contacts[curname][3])


def delete():
    curname = shown_contacts.selection_get()
    del contacts[curname]

    update_listbox()


def save():
    contacts_file = tkinter.filedialog.asksaveasfile()
    ## Check if empty, then save 'contacts' dict to file
    if contacts_file is not None:
        print(contacts, file=contacts_file)
    

def load():
    global contacts
    contacts_file = tkinter.filedialog.askopenfile()
    if contacts_file is not None:
        content = contacts_file.readline()
        contacts = eval(content)  ## Convert text to list, dict, etc.
    update_listbox()

    


title = tkinter.Label(screen, text="My Address Book")
open_btn = tkinter.Button(screen, text="Open", command=load)

shown_contacts = tkinter.Listbox(screen)  # Listbox

shown_contacts.bind("<<ListboxSelect>>", edit)

show_btn = tkinter.Button(screen, text="Show", command=show)
del_btn = tkinter.Button(screen, text="Delete", command=delete)
name_L = tkinter.Label(screen, text="Name:")
add_L = tkinter.Label(screen, text="Address:")
mob_L = tkinter.Label(screen, text="Mobile:")
email_L = tkinter.Label(screen, text="Email:")
birth_L = tkinter.Label(screen, text="Birthday:")
update_btn = tkinter.Button(screen, text="Update/Add", command=update)
save_btn = tkinter.Button(screen, text="Save", command=save)

name_E = tkinter.Entry(screen)
add_E = tkinter.Entry(screen)
mob_E = tkinter.Entry(screen)
email_E = tkinter.Entry(screen)
birth_E = tkinter.Entry(screen)

title.grid(row=0, column=0)
open_btn.grid(row=0, column=2)
shown_contacts.grid(row=1, column=0, rowspan=5, columnspan=2)
name_L.grid(row=1, column=2)
add_L.grid(row=2, column=2)
mob_L.grid(row=3, column=2)
email_L.grid(row=4, column=2)
birth_L.grid(row=5, column=2)
show_btn.grid(row=6, column=0)
del_btn.grid(row=6, column=1)
update_btn.grid(row=6, column=3)
save_btn.grid(row=7, column=1, columnspan=2)

name_E.grid(row=1, column=3)
add_E.grid(row=2, column=3)
mob_E.grid(row=3, column=3)
email_E.grid(row=4, column=3)
birth_E.grid(row=5, column=3)

screen.mainloop()
