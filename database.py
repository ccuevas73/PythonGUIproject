#import sqlite3 functions
import sqlite3

#import os functions
import os

#import person class
from Person import *

#creates database to start if it doesn't exist
def init_database():
    #get connection to database
    connection = get_connection()
    
    #get cursor for sql execution
    cursor = connection.cursor()

    #sql command for creating a table - does not create table if it already exists
    command = "CREATE TABLE IF NOT EXISTS person(id BIGINT, first_name TEXT, last_name TEXT, email TEXT)"

    #execute sql command
    cursor.execute(command)

#gets connection to database
def get_connection():
    #get the folder path for wherever this file is
    cwd = os.path.dirname(os.path.realpath(__file__))
    
    #returns connection to person.db file in same folder as this file
    #will create person.db file if it doesn't exist
    return sqlite3.connect(cwd + r"\person.db")

#loads all contacts from database
def load():
    #initialize empty array
    contacts = []
    
    #sql query for selecting all person records
    command = 'SELECT * FROM person'

    #get connection to database
    connection = get_connection()

    #get cursor for sql execution
    cursor = connection.cursor()

    #execute sql command
    cursor.execute(command)

    #returns all rows returned from sql query
    rows = cursor.fetchall()
    
    #for each row returned, add new person with that data to contacts array
    for row in rows:
        contacts.append(person(row[0], row[1], row[2], row[3]))
    
    #return contacts array
    return contacts

#inserts person into database
def insert(person: person):
    #calls the set_id method on person which creates a random id 
    person.set_id()

    #sql command for inserting a person
    command = """INSERT INTO person
                  (id, first_name, last_name, email) 
                  VALUES 
                  (?, ?, ?, ?)"""

    #get connection to database              
    connection = get_connection()

    #get cursor for sql execution
    cursor = connection.cursor()
    
    #execute sql command and passes in person object field values
    cursor.execute(command,(person.get_id(), person.get_first_name(), person.get_last_name(), person.get_email()))

    #commit the command to database
    connection.commit()

    #close cursor and connection
    cursor.close()
    connection.close()
   
#updates person in database
def update(person: person):
    #sql command for updating a person
    command = """UPDATE person SET 
                 first_name = ?, last_name = ?, email = ?
                 WHERE id = ?"""

    #get connection to database             
    connection = get_connection()

    #get cursor for sql execution
    cursor = connection.cursor()
    
    #execute sql command and passes in person object field values
    cursor.execute(command, (person.get_first_name(), person.get_last_name(), person.get_email(), person.get_id()))
    
    #commit the command to database
    connection.commit()

    #close cursor and connection
    cursor.close()
    connection.close()

def delete(person: person):
    command = "DELETE FROM person WHERE id = ?"

    #get connection to database
    connection = get_connection()

    #get cursor for sql execution
    cursor = connection.cursor()
    
    #execute sql command and pass in person id
    cursor.execute(command, (person.get_id(),))
    
    #commit the command to database
    connection.commit()
    
    #close cursor and connection
    cursor.close()
    connection.close()