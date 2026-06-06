class Customer:
    
    def __init__(self, name, cnic, phone):
        self.__name = name
        self.__cnic = cnic
        self.__phone = phone
        self.__accounts = []

    def get_account_holder_name(self):
        return self.__name
    
    def get_account_holder_cnic(self):
        return self.__cnic
    
    def get_account_holder_phone(self):
        return self.__phone
    
    def add_account(self,account):
        if account not in self.__accounts:
            self.__accounts.append(account)
            print(f"Account added successfully!")
        else:
            print("Account Already Exists!")
    
    def get_account(self):
        return self.__accounts
    
    def display_info(self):
            print("===========================")
            print("   CUSTOMER DETAILS")
            print("===========================")
            print(f"Name           : {self.get_account_holder_name()}")
            print(f"CNIC           : {self.get_account_holder_cnic()}")
            print(f"Phone          : {self.get_account_holder_phone()}")
            print(f"Total Account  : {len(self.__accounts)}")
            print("===========================")

            for i, account in enumerate(self.__accounts, 1):
                print(f"---- Account {i} ----")
                account.display_info()

    
    
    
