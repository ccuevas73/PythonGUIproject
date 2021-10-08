import sqlite3
import os
from Person import *

def init_database():

    connection = get_connection()
    

     
    cursor = connection.cursor()

    command = "CREATE TABLE IF NOT EXISTS person(id BIGINT, first_name TEXT, last_name TEXT, email TEXT)"
    cursor.execute(command)

def get_connection():

    cwd = os.path.dirname(os.path.realpath(__file__))
    
    return sqlite3.connect(cwd + r"\person.db")

def load():
    contacts = []
    
    command = 'SELECT * FROM person'
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(command)
    rows = cursor.fetchall()
    
    
    for row in rows:
        contacts.append(person(row[0], row[1], row[2], row[3]))
    
    return contacts

def insert(person: person):
    person.set_id()
    command = """INSERT INTO person
                  (id, first_name, last_name, email) 
                  VALUES 
                  (?, ?, ?, ?)"""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(command,(person.get_id(), person.get_first_name(), person.get_last_name(), person.get_email()))
    connection.commit()
    cursor.close()
    connection.close()
    # update people in db

def delete(person: person):
    command = "DELETE FROM person WHERE id = ?"
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(command, (person.get_id(),))
    connection.commit()
    cursor.close()
    connection.close()