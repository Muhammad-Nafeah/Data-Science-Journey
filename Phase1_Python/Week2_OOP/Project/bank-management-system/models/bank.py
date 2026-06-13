class Bank:
    
    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.__customers = []

    def add_customer(self,customer):
        if customer not in self.__customers:
            self.__customers.append(customer)
            print("Customer Added Successfully!")
        else:
            print("Customer Already Exists!")
    
    def find_customer(self, cnic):
        for customer in self.__customers:
            if customer.get_account_holder_cnic() == cnic:
                return customer
        print("Customer Not Found!")

    def find_account(self, account_number):
        for customer in self.__customers:
            for account in customer.get_account():
                if account.get_account_number() == account_number:
                    return account
        print("Account Not Found!")

    def transfer(self, from_account_number, to_account_number, amount):

        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if from_account and to_account:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"Rs.{amount} transferred successfully!")
        else:
            print("Transfer failed! Account not found.")

    def display_all_customers(self):

        for customer in self.__customers:
            customer.display_info()

    def total_deposit(self):

        total = 0
        for customer in self.__customers:
            for account in customer.get_account():
                total += account.get_account_balance()
        print(f"Total Deposits: Rs.{total}")
