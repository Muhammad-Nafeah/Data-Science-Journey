from datetime import datetime

class Transaction:

    def __init__(self, transaction_id, account_number, account_type, amount):
        self.__transaction_id = transaction_id
        self.__account_number = account_number
        self.__account_type = account_type
        self.__amount = amount
        self.__date = datetime.now()

    def get_transaction_id(self):
        return self.__transaction_id
    
    def get_account_number(self):
        return self.__account_number
    
    def get_account_type(self):
        return self.__account_type
    
    def get_amount(self):
        return self.__amount
    
    def get_date(self):
        return self.__date
    
    def display_transaction(self):
            print("===========================")
            print("   TRANSACTION DETAILS")
            print("===========================")
            print(f"Transaction ID : {self.get_transaction_id()}")
            print(f"Account Number : {self.get_account_number()}")
            print(f"Type           : {self.get_account_type()}")
            print(f"Amount         : Rs.{self.get_amount()}")
            print(f"Date           : {self.get_date()}")
            print("===========================")
    