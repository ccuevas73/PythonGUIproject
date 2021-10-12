#import tkinter GUI library
from tkinter import *

#import messagebox from tkinter
from tkinter import messagebox

#import person class
from Person import *

import os

#padding values for multiple widgets
__pady = 2
__padx = 2

#opens up the contact_info window
#takes a contact/person, a parent window, and whether or not this is for a new (added) contact
def init(root: Tk, contact: person, isAdd: bool) -> Toplevel:
    init_contact(contact)
    init_window(root, isAdd)

    #returns this contact_info window so it can be waited on
    return current_window

#sets global contact variable
def init_contact(contact: person):
    global current_contact
    current_contact = contact

#sets up new contact_info window
def init_window(root: Tk, isAdd: bool):
    #sets global parent window variable
    global main_window
    main_window = root

    #creates new contact_info window and sets the global current window variable
    global current_window
    current_window = Toplevel(main_window)
    cwd = os.path.dirname(os.path.realpath(__file__))
    current_window.iconbitmap(cwd + r"\favicon2.ico")
    #locks input and focus on new window
    current_window.grab_set()

    __init__controls(isAdd)

#sets up controls on the new contact_info window
def __init__controls(isAdd: bool):
    #creates first_name_text entry box
    global first_name_text
    first_name_text = Entry(current_window)
    first_name_text.grid(row=1, column=1, padx=__padx, pady=__pady)

    #sets entry box text to person first name value
    first_name_text.insert(END, current_contact.get_first_name())

    #creates last_name_text entry box
    global last_name_text
    last_name_text = Entry(current_window)
    last_name_text.grid(row=1, column=2, padx=__padx, pady=__pady)

    #sets entry box text to person last name value
    last_name_text.insert(END, current_contact.get_last_name())
    

    #creates email_text entry box
    global email_text
    email_text = Entry(current_window)
    email_text.grid(row=2, column=1, columnspan=2, sticky='nesw', padx=__padx, pady=__pady)

    #sets entry box text to person email value
    email_text.insert(END, current_contact.get_email())

    #creates save button
    global save_button
    save_button = Button(current_window, text='Save', command=__save_contact)
    save_button.grid(row=3, column=1, padx=__padx, pady=__pady)

    #creates exit button
    if not isAdd:
        global delete_button
        delete_button = Button(current_window, text="Delete", command=__delete_contact)
        delete_button.grid(row=3, column=2, padx=__padx, pady=__pady)

#saves contact when save button clicked
def __save_contact():
    #first creates new person with entered values from contact_info widgets
    temp_person = person(0, first_name_text.get(), last_name_text.get(), email_text.get())

    #checks if entered values are invalid
    if temp_person.get_is_person_invalid():
        #if invalid, disable all controls
        __disable_all_controls()

        #then show error popup
        messagebox.showerror("Error", "Invalid Entry, Please try again.")

        #then reenable all controls
        __enable_all_controls()
    else:
        #otherwise overwrite current contact with entered values
        current_contact.overwrite(temp_person)

        #then close window
        current_window.destroy()

#delete contact when delete button pressed
def __delete_contact():
    #set deleted boolean to true on contact
    #actual delete handled elsewhere
    current_contact.set_is_deleted(True)

    #close window
    __close_window()

#disables all controls
def __disable_all_controls():
    #loop through all controls in contact_info
    for w in current_window.winfo_children():
        #set them to disabled
        w.configure(state = DISABLED)

    #bypass the WM_DELETE_WINDOW event ('x' click in top right)
    current_window.protocol('WM_DELETE_WINDOW', __disable_event)

#enables all controls
def __enable_all_controls():
    #loop through all controls in contact_info
    for w in current_window.winfo_children():
        #set then to enabled
        w.configure(state = NORMAL)

    #reset the WM_DELETE_WINDOW event ('x' click in top right) to close the window
    current_window.protocol('WM_DELETE_WINDOW', __close_window)

#does nothing
def __disable_event():
    pass

#closes current window
def __close_window():
    current_window.destroy()
