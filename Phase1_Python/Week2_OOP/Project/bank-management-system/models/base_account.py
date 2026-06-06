from abc import ABC, abstractmethod

class BaseAccount(ABC):

    def __init__(self, account_number, account_balance, account_type):
        self.__account_number = account_number
        self.__account_balance = account_balance
        self.__account_type = account_type

    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_account_balance(self):
        return self.__account_balance

    def get_account_type(self):
        return self.__account_type

    def get_account_number(self):
        return self.__account_number
    
    def set_account_balance(self, new_balance):
        self.__account_balance = new_balance
    

    def display_info(self):
        print(f"Account Number: {self.get_account_number()}\nAccount Type: {self.get_account_type()}\nBalance: {self.get_account_balance()}")


