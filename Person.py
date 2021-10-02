class person:
    def __init__(self, first_name: str='', last_name: str='', email: str=''):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

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