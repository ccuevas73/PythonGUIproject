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

add_button = Button(main_window, text='add', command=add_contact)
exit_button = Button(main_window, text="Exit", command=main_window.destroy)

contact_list.pack()
add_button.pack()
exit_button.pack()


contact_list.pack()
exit_button.pack()

def populate_contacts():
    contacts.clear()
    contacts.append(person('jake', 'turd', 'colts@oops.com'))
    contacts.append(person('i', 'forgot', 'thiswasincommits@aol.com'))
    contacts.append(person('jordon', 'dfsdf', 'fdasfs@aol.com'))
    contacts.append(person('fasdfs', 'summer', 'summers@yahoo.com'))
    contacts.append(person('francis', 'doessucktho', 'adf@aol.com'))

    contact_list.delete(0, END)

    for c in contacts:
        contact_list.insert(END, c)



main_window.after(0, populate_contacts)
main_window.mainloop()


