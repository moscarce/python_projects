from pythonProject.oop.bank_app.account import Account


class Bank:
    def __init__(self, bank_name: str):
        self.__bank_name = bank_name
        self.__accounts = []

    def register(self, first_name: str, last_name: str, pin: str):
        name = f'{first_name} {last_name}'
        account = Account(self.__generate_account_number(), name, pin)
        self.__accounts.append(account)
        print(f'''
Account created successfully
Here are you account info

=======================================================
account name: {account.get_account_name()}
account number: {account.get_account_number()}
=======================================================
''')

    def __generate_account_number(self):
        return str(2337167890 + len(self.__accounts) + 10)

    def get_account(self, account_number):
        return self.__find_account(account_number)

    def __find_account(self, account_number):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        raise ValueError('Account not found')

    def deposit(self, amount, account_number):
        self.__find_account(account_number).deposit(amount)

    def check_balance(self, account_number, pin):
        return self.__find_account(account_number).get_balance(pin)

    def withdraw(self, amount, account_number, pin):
        self.__find_account(account_number).withdraw(amount, pin)

    def transfer(self, amount, from_account, to_account, pin):
        self.__find_account(from_account).withdraw(amount, pin)
        self.__find_account(to_account).deposit(amount)
