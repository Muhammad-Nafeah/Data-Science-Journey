from models.base_account import BaseAccount

class SavingAccount(BaseAccount):

    def __init__(self, account_number, account_balance, interest_rate):
        super().__init__(account_number, account_balance, "Savings")
        self.__interest_rate = interest_rate

    def deposit(self, amount):
        new_balance = self.get_account_balance() + amount
        self.set_account_balance(new_balance)
        print(f"Deposited Rs.{amount}. New Balance: Rs.{new_balance}")
        

    def withdraw(self, amount):
        if self.get_account_balance() - amount >= 1000:
            new_balance = self.get_account_balance() - amount
            self.set_account_balance(new_balance)
            print(f"Withdraw Rs.{amount}. New Balance: Rs.{new_balance}")
        else:
            print(f"Warning! Minimum balance must be Rs.1000. Current Balance: Rs.{self.get_account_balance()}")
    
    def add_interest(self):
        interest = (self.get_account_balance() * self.__interest_rate) / 100
        new_balance = self.get_account_balance() + interest
        self.set_account_balance(new_balance)
        print(f"Interest of Rs.{interest} added. New Balance: Rs.{new_balance}")

