from pythonProject.oop.Diaries.custom_exception.diary_not_found import DiaryNotFound
from pythonProject.oop.Diaries.custom_exception.incorrect_password import IncorrectPassword
from pythonProject.oop.Diaries.diaries import Diaries
from pythonProject.oop.Diaries.entry_not_found import EntryNotFound

diaries = Diaries()


def display(message):
    print(message)


def collect_input(message):
    return input(message)


def add_entry(diary):
    title = collect_input("what's the title of the entry: ")
    body = collect_input("Oya gist us: ")
    diary.create_entry(title, body)
    display('Entry created successfully')
    logged_in_page(diary)


def collect_entry_id(param):
    user_id = input(param)
    while not user_id.isdigit():
        display('Invalid, id can only be in digit')
        user_id = input(param)
    return int(user_id)


def find_entry_by_id(diary):
    entry_id = collect_entry_id('What is the diary ID: ')
    try:
        entry = diary.find_entry_by_id(entry_id)
        print(entry)
        logged_in_page(diary)
    except EntryNotFound:
        display('Entry not found')
        logged_in_page(diary)


def update_entry(diary):
    entry_id = collect_entry_id('What is the entry ID: ')
    try:
        diary.find_entry_by_id(entry_id)
        title = collect_input('Title please: ')
        body = collect_input("oya gist us: ")
        diary.update_entry(entry_id, title, body)
        display('Entry updated successfully')
        logged_in_page(diary)
    except EntryNotFound:
        display('Entry not found')
        logged_in_page(diary)


def delete_entry(diary):
    entry_id = collect_entry_id('What is the entry ID: ')
    try:
        diary.find_entry_by_id(entry_id)
        diary.delete_entry(entry_id)
        display('Entry deleted')
        logged_in_page(diary)
    except EntryNotFound:
        display('Entry not found')
        logged_in_page(diary)


def show_all_entry(diary):
    diary.show_all_entry()
    logged_in_page(diary)


def logged_in_page(diary):
    message = '''
1 -> Add Entry
2 -> Find Entry by id
3 -> Update Entry
4 -> Show all entry
5 -> Delete Entry
6 -> Logout
    '''
    collected_input = collect_input(message)
    match collected_input:
        case '1':
            add_entry(diary)
        case '2':
            find_entry_by_id(diary)
        case '3':
            update_entry(diary)
        case '4':
            show_all_entry(diary)
        case '5':
            delete_entry(diary)
        case '6':
            home()
        case _:
            display('Invalid input')
            logged_in_page(diary)


def login():
    username = collect_input('Enter username: ')
    try:
        diary = diaries.find_by_username(username)
        password = collect_input('Enter password: ')
        diary.unlock_diary(password)
        logged_in_page(diary)
    except DiaryNotFound:
        display('Username not found')
        home()
    except IncorrectPassword:
        display('Incorrect password')
        home()


def create_diary():
    username = collect_input('Enter username: ')
    password = collect_input('Enter password: ')
    display('Diary created successfully')
    diaries.add(username, password)
    diary = diaries.find_by_username(username)
    diary.unlock_diary(password)
    logged_in_page(diary)


def home():
    message = '''
Welcome to MUMU diaries

1 -> Login
2 -> Create diary
3 -> Exit
    '''
    display(message)
    collected_input = collect_input('')
    match collected_input:
        case '1':
            login()
        case '2':
            create_diary()
        case '3':
            display('Thanks')
            exit(69)
        case _:
            display('Invalid input')
            home()


home()
