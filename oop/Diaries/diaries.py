from pythonProject.oop.Diaries.custom_exception.diary_not_found import DiaryNotFound
from pythonProject.oop.Diaries.custom_exception.incorrect_password import IncorrectPassword
from pythonProject.oop.Diaries.dairy import Diary


class Diaries:
    def __init__(self):
        self.__diaries = []

    def add(self, username: str, password: str):
        diary = Diary(username, password)
        self.__diaries.append(diary)

    def find_by_username(self, username):
        for diary in self.__diaries:
            if diary.get_username() == username:
                return diary
        raise DiaryNotFound()

    def delete(self, username, password):
        diary = self.find_by_username(username)
        if diary.get_password() == password:
            self.__diaries.remove(diary)
        else:
            raise IncorrectPassword()
