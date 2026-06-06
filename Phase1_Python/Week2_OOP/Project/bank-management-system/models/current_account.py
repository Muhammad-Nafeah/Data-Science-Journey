from models.base_account import BaseAccount

class CurrentAccount(BaseAccount):

    def __init__(self, account_number, account_balance, overdraft_limit):
        super().__init__(account_number, account_balance, "Current")
        self.__overdraft_limit = overdraft_limit

    def deposit(self, amount):
        new_balance = self.get_account_balance() + amount
        self.set_account_balance(new_balance)
        print(f"Deposited Rs.{amount}. New Balance: Rs.{new_balance}")

    def withdraw(self, amount):
        if self.get_account_balance() - amount >= -self.__overdraft_limit:
            new_balance = self.get_account_balance() - amount
            self.set_account_balance(new_balance)
            print(f"Withdraw Rs.{amount}. New Balance: Rs.{new_balance}")
        else:
            print(f"Warning! Overdraft Limit Exceeded. Current Balance: Rs.{self.get_account_balance()}")

    def display_info(self):
        super().display_info()
        print(f"Overdraft Limit: {self.__overdraft_limit}")
        