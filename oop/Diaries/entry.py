import datetime


class Entry:
    def __init__(self, id:int,title:str, body:str):
        self.__body = body
        self.__title = title
        self.__entry_id = id
        self.__date_created = datetime.datetime.now().strftime("%Y-%m-%d")

    def get_entry_id(self):
        return self.__entry_id

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def set_title(self,title):
        self.__title = title

    def set_body(self,body):
        self.__body = body


    def __str__(self):
        return f"""
**********************************************************************************
{self.__title}
{self.__body}

ENTRY ID = {self.__entry_id}
**********************************************************************************
        """






