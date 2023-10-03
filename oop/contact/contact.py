import re


class NotANumber(Exception):

    def __init__(self, *args) -> None:
        super().__init__(*args)


class NotAMail(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class Contact():
    def __init__(self):
        self._name = ''
        self._address = ''
        self._telephone = ''
        self._email = ''

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_address(self, address):
        self._address = address

    def get_address(self):
        return self._address

    def set_telephone(self, telephone:str ):
        if telephone.isdigit():
            self._telephone = telephone
        else:
            raise NotANumber()

    def get_telephone(self):
        return self._telephone

    def set_email(self, email):
        if self._validate_mail(email):
            self._email = email
        else:
            raise NotAMail()

    def get_email(self):
        return self._email

    def _validate_mail(self, email):
        return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))


