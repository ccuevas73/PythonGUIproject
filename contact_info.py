from tkinter import *
from Person import *

__pady = 2
__padx = 2

def init(root: Tk, contact: person):
    init_contact(contact)
    init_window(root)

def init_contact(contact: person):
    global current_contact
    current_contact = contact


def init_window(root: Tk):
    global main_window
    main_window = root

    global current_window
    current_window = Toplevel(main_window)
    current_window.grab_set()

    __init__controls()

def __init__controls():
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
    save_button = Button(current_window, Text='Save')
    save_button.grid(row=3, column=1, padx=__padx, pady=__pady)

    global delete_button
    delete_button = Button(current_window, Text='Delete')
    delete_button.grid(row=3, column=2, padx=__padx, pady=__pady)


