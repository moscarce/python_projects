from pythonProject.oop.Diaries.custom_exception.incorrect_password import IncorrectPassword
from pythonProject.oop.Diaries.entry_not_found import EntryNotFound
from pythonProject.oop.Diaries.entry import Entry


class Diary:
    def __init__(self, username: str, password: str):
        self.__password = password
        self.__username = username
        self.__is_locked = True
        self.__entries = []

    def is_locked(self):
        return self.__is_locked

    def unlock_diary(self,password):
        if self.__password == password:
            self.__is_locked = False
        else:
            raise IncorrectPassword()

    def lock_diary(self):
        self.__is_locked = True

    def create_entry(self, title: str, body: str):
        id = self.__generate_id()
        entry = Entry(id , title, body)
        self.__entries.append(entry)
        print(f'ID = {id}')

    def __generate_id(self):
        return int(len(self.__entries) + 1)

    def show_all_entry(self):
        for entry in self.__entries:
            print(entry)

    def find_entry_by_id(self, id_passed: int):
        for entry in self.__entries:
            if entry.get_entry_id() == id_passed:
                return entry
        raise EntryNotFound

    def entries_size(self):
        return len(self.__entries)

    def delete_entry(self, id_passed):
        entry = self.find_entry_by_id(id_passed)
        self.__entries.remove(entry)

    def update_entry(self, id_passed, title, body):
        entry = self.find_entry_by_id(id_passed)
        entry.set_title(title)
        entry.set_body(body)

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
