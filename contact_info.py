from tkinter import *
from tkinter import messagebox
from Person import *

__pady = 2
__padx = 2

def init(root: Tk, contact: person, isAdd: bool) -> Toplevel:
    init_contact(contact)
    init_window(root, isAdd)
    return current_window

def init_contact(contact: person):
    global current_contact
    current_contact = contact


def init_window(root: Tk, isAdd: bool):
    global main_window
    main_window = root

    global current_window
    current_window = Toplevel(main_window)
    current_window.grab_set()

    __init__controls(isAdd)

def __init__controls(isAdd: bool):
    global first_name_text
    first_name_text = Entry(current_window)
    first_name_text.grid(row=1, column=1, padx=__padx, pady=__pady)
    first_name_text.insert(END, current_contact.get_first_name())

    global last_name_text
    last_name_text = Entry(current_window)
    last_name_text.grid(row=1, column=2, padx=__padx, pady=__pady)
    last_name_text.insert(END, current_contact.get_last_name())
    

    global email_text
    email_text = Entry(current_window)
    email_text.grid(row=2, column=1, columnspan=2, sticky='nesw', padx=__padx, pady=__pady)
    email_text.insert(END, current_contact.get_email())

    global save_button
    save_button = Button(current_window, text='Save', command=__save_contact)
    save_button.grid(row=3, column=1, padx=__padx, pady=__pady)

    if not isAdd:
        global delete_button
        delete_button = Button(current_window, text="Delete", command=__delete_contact)
        delete_button.grid(row=3, column=2, padx=__padx, pady=__pady)

    

def __save_contact():

    temp_person = person(0, first_name_text.get(), last_name_text.get(), email_text.get())
    if temp_person.get_is_person_invalid():
        __disable_all_controls()
        messagebox.showerror("Error", "Invalid Entry, Please try again.")
        __enable_all_controls()
    else:
        current_contact.overwrite(temp_person)
        current_window.destroy()

def __delete_contact():
    current_contact.set_is_deleted(True)
    __close_window()

def __disable_all_controls():
    for w in current_window.winfo_children():
        w.configure(state = DISABLED)

    current_window.protocol('WM_DELETE_WINDOW', __disable_event)

def __enable_all_controls():
    for w in current_window.winfo_children():
        w.configure(state = NORMAL)

    current_window.protocol('WM_DELETE_WINDOW', __close_window)


def __disable_event():
    pass

def __close_window():
    current_window.destroy()
