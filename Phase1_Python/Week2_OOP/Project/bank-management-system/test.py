from models.savings_account import SavingAccount
from models.current_account import CurrentAccount
from models.customer import Customer
from models.bank import Bank

# create bank
bank = Bank("Meridian Bank")

# create customers
nafeah = Customer("Abdul Nafeah", "42101-1234567-1", "0312-1234567")
ali = Customer("Ali Ahmed", "42101-7654321-1", "0333-7654321")

# create accounts
savings = SavingAccount("PKR-001", 50000, 5)
current = CurrentAccount("PKR-002", 30000, 10000)

# add accounts to customers
nafeah.add_account(savings)
nafeah.add_account(current)

# add customers to bank
bank.add_customer(nafeah)
bank.add_customer(ali)

# test transactions
savings.deposit(10000)
savings.withdraw(5000)
savings.add_interest()
current.deposit(20000)
current.withdraw(55000)

# test transfer
bank.transfer("PKR-001", "PKR-002", 5000)

# display everything
bank.display_all_customers()
bank.total_deposit()




  