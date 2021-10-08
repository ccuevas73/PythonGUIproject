from tkinter import *
from Person import *
import database

import contact_info

contacts = []

def onselect(evt):
    w = evt.widget
    current_selection = w.curselection()

    if len(current_selection) == 0:
        return
        
    index = int(current_selection[0])

    if len(contacts) == 0:
        return

    selected_contact = contacts[index]

    dialog = contact_info.init(main_window, selected_contact, False)
    main_window.wait_window(dialog)

    contact_list.delete(index)

    if selected_contact.get_is_deleted():
        database.delete(selected_contact)
        del contacts[index]
    else:
        contact_list.insert(index, selected_contact)

def add_contact():
    new_contact = person()
    dialog = contact_info.init(main_window, new_contact, True)

    main_window.wait_window(dialog)

    if not new_contact.get_is_person_invalid():
        database.insert(new_contact)
        contacts.append(new_contact)
        contact_list.insert(END, new_contact)


main_window = Tk()

contact_list = Listbox(main_window, selectmode=SINGLE)
contact_list.bind('<<ListboxSelect>>', onselect)

add_button = Button(main_window, text='Add', command=add_contact)
exit_button = Button(main_window, text="Exit", command=main_window.destroy)

contact_list.pack()
add_button.pack()
exit_button.pack()


contact_list.pack()
exit_button.pack()

def populate_contacts():
    database.init_database()
    dbcontacts = database.load()
    
    contacts.clear()
    contacts.extend(dbcontacts)

    contact_list.delete(0, END)

    for c in contacts:
        contact_list.insert(END, c)




main_window.after(0, populate_contacts)
main_window.mainloop()


