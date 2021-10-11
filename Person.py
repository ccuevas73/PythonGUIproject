import re
import random

class person:
    #constructor for person
    def __init__(self, id: int=0, first_name: str='', last_name: str='', email: str=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_deleted = False
        self.id = id

    #string conversion for person
    def __str__(self):
        return self.get_full_name()

    #getter for first_name
    def get_first_name(self):
        return self.first_name

    def set_first_name(self, value: str):
        self.first_name = value

    def set_last_name(self, value: str):
        self.last_name = value

    def set_email(self, value: str):
        self.email = value

    #getter for id
    def get_id(self):
        return self.id

    def set_id(self):
        self.id = random.randrange(100000000, 999999999)

        

    
    #getter for last name
    def get_last_name(self):
        return self.last_name

    #getter for full name
    def get_full_name(self):
        return self.get_first_name() + "  " + self.get_last_name()

    #getter for email
    def get_email(self):
        return self.email

    
    #getter for is_deleted
    def get_is_deleted(self):
        return self.is_deleted

    def set_is_deleted(self, value: str):
        self.is_deleted = value

    #getter for if a person is invalid
    def get_is_person_invalid(self):
        #first and last name must be populated and cannot be white space
        is_first_name_blank = not self.first_name or self.first_name.isspace()
        is_last_name_blank = not self.last_name or self.last_name.isspace()
        return is_first_name_blank or is_last_name_blank or self.is_email_invalid()

    #getter for is email invalid
    def is_email_invalid(self):
        #if email is blank then it is valid, email is not a mandatory field
        if not self.email:
            return False
        else:
            #if email is not blank then it must match xxxx@xxxx.xxxx
            return not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", self.email)
            
    #set this persons field values to another persons values
    def overwrite(self, other):
        self.first_name = other.first_name
        self.last_name = other.last_name
        self.email = other.email