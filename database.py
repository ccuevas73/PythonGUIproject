import sqlite3
import os

def init_database():
    cwd = os.path.dirname(os.path.realpath(__file__))
    global connection
    connection = sqlite3.connect(cwd + r"\person.db")

    global cursor 
    cursor = connection.cursor()

    command1 = "CREATE TABLE IF NOT EXISTS person(first_name TEXT, last_name TEXT, email TEXT)"
    cursor.execute(command1)

    # load people from db

    # insert people to db

    # update people in db

    # delete people from db