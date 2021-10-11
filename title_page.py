#Contracts App
#Carlos Cuevas
#10-11-2021 version 1.0
#The purpose of this program is to allow a user to add, edit, delete a contact they wish to store //
#it will store their contact in a database for future use



from tkinter import *
from Person import *
import database

import contact_info

#creates empty global contacts array

contacts = []

#onselect to handle item selection in listbox
#evt parameter passed in has info from listbox selection

def onselect(evt):
    
    #get listbox widget from evt parameter
    
    w = evt.widget
    
    #get the listbox widget's selection

    current_selection = w.curselection()

    #if the nothing selected then do nothing else
    
    if len(current_selection) == 0:
        return
        
    #get index from selected listbox item
    #selected item is at first index since only one item can be selected at a time
    
    index = int(current_selection[0])

    #if global contacts array is empty then do nothing else
    
    if len(contacts) == 0:
        return

    #set selected_contact to the person in the contacts array using the selected item index
    #the contacts array and the listbox items are in the same order so the index is the same between the two
    
    selected_contact = contacts[index]

    #create new contact_info window passing in selected_contact
    
    dialog = contact_info.init(main_window, selected_contact, False)
    
    #wait for the contact_info window to close
    
    main_window.wait_window(dialog)

    #delete the selected item from the listbox
    #if the contact has been updated in the contact_info window then it has to be removed and readded for the updates to show up in the GUI
    
    contact_list.delete(index)

    #check if the selected contact is set to be deleted
    
    if selected_contact.get_is_deleted():

        #if it is being deleted, delete from database
        database.delete(selected_contact)
        
        #delete from the global contacts array
        del contacts[index]
    else:
        #if not being deleted, update contact in database
        database.update(selected_contact)
        #put updated contact back into listbox
        contact_list.insert(index, selected_contact)

#add_contact to handle add button click
def add_contact():
    #create new person object
    new_contact = person()
    #create new contact_info window and pass in new person object
    dialog = contact_info.init(main_window, new_contact, True)

    #wait for the contact_info window to close
    main_window.wait_window(dialog)

    #check if contact is not invalid
    if not new_contact.get_is_person_invalid():
        #if valid, insert to database
        database.insert(new_contact)
        #add contact to global contacts array
        contacts.append(new_contact)
        #insert to listbox
        contact_list.insert(END, new_contact)

#create the main window Tk
main_window = Tk()

#create listbox for contacts and set the selection mode to single item only
contact_list = Listbox(main_window, selectmode=SINGLE)
#bind listbox selection to onselect function
contact_list.bind('<<ListboxSelect>>', onselect)

#create add button
add_button = Button(main_window, text='Add', command=add_contact)
#creates exit button
exit_button = Button(main_window, text="Exit", command=main_window.destroy)

#packs widgets in order
contact_list.pack()
add_button.pack()
exit_button.pack()

#repack
contact_list.pack()
exit_button.pack()

#populates contacts from database
def populate_contacts():
    #initialize the database
    database.init_database()
    #load contacts into a new dbcontacts array
    #if loaded straight into global contacts array then they get dropped from memory after function ends
    dbcontacts = database.load()
    #clear contacts array in case it has items in it
    contacts.clear()
    #add all database contacts into global contacts array
    contacts.extend(dbcontacts)

    #clear listbox in case it has items in it
    contact_list.delete(0, END)
    #for each contact add to the listbox
    for c in contacts:
        contact_list.insert(END, c)



#set the populate_contacts function to run after main window shown
main_window.after(0, populate_contacts)
#show in main window
main_window.mainloop()


