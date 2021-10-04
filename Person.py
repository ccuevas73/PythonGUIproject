import re

class person:
    def __init__(self, first_name: str='', last_name: str='', email: str=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_deleted = False

    def __str__(self):
        return self.get_full_name()

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, value: str):
        self.first_name = value

    def set_last_name(self, value: str):
        self.last_name = value

    def set_email(self, value: str):
        self.email = value
    

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return self.get_first_name() + "  " + self.get_last_name()

    def get_email(self):
        return self.email

    

    def get_is_deleted(self):
        return self.is_deleted

    def set_is_deleted(self, value: str):
        self.is_deleted = value

    def get_is_person_invalid(self):
        is_first_name_blank = not self.first_name or self.first_name.isspace()
        is_last_name_blank = not self.last_name or self.last_name.isspace()
        return is_first_name_blank or is_last_name_blank

    def is_email_invalid(self):
        if not self.email:
            return False
        else:
            return not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)
            

    def overwrite(self, other):
        self.first_name = other.first_name
        self.last_name = other.last_name
        self.email = other.email