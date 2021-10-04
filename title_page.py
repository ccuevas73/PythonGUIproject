from tkinter import *
from Person import *

import contact_info

contacts = []

def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    selected_contact = contacts[index]

    dialog = contact_info.init(main_window, selected_contact, False)
    main_window.wait_window(dialog)

    contact_list.delete(index)

    if selected_contact.get_is_deleted():
        del contacts[index]
    else:
        contact_list.insert(index, selected_contact)

def add_contact():
    new_contact = person()
    dialog = contact_info.init(main_window, new_contact, True)

    main_window.wait_window(dialog)

    if not new_contact.get_is_person_invalid():
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
    contacts.clear()
    contacts.append(person('jake', 'turner', 'colts10@yahoo.com'))
    contacts.append(person('duckworth', 'horgan', 'chargers@yahoo.com'))
    contacts.append(person('jordon', 'fisher', 'rams@aol.com'))
    contacts.append(person('tyrone', 'morson', 'lions@yahoo.com'))
    contacts.append(person('francis', 'edgerton', 'thedolphins@gmail.com'))

    contact_list.delete(0, END)

    for c in contacts:
        contact_list.insert(END, c)



main_window.after(0, populate_contacts)
main_window.mainloop()


