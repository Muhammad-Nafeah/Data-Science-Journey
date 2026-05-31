'''Basic Encapsulation
Take your BankAccount class from Day 1. Make balance private. 
Add a get_balance() method and a deposit() and withdraw() that 
work through the private attribute.'''


class BankAccount:

    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        print(self.__balance)
        return self.__balance
    
    def deposit(self,amount):
        self.__balance += amount
        print(f"Deposit Rs.{amount}. New Balance Rs.{self.__balance}")

    def withdraw(self,amount):
        if amount > self.__balance:
            print(f"Insufficient Balance! You only have Rs.{self.__balance}")
        else:
            self.__balance -= amount
            print(f"Withdraw Rs.{amount}. New Balance Rs.{self.__balance}")
account = BankAccount()
account.deposit(10000000)
account.withdraw(200000)
account.get_balance()


'''DS Theme
Create a class DataSet with a private attribute __data (a list of numbers). 
Add a get_data() method and an add_data(value) method that only adds the value 
if it's a number, otherwise prints a warning.'''


class DataSet:
    def __init__(self):
        self.__data = []
    
    def get_data(self):
        print(self.__data)
        return self.__data
    
    def add_data(self,value):
        if type(value) == int or type(value) == float:
        #if isinstance(value, (int, float)):  same as above line
            self.__data.append(value)
        else:
            print(f"Warning!\n'{value}' is not a number!")

dataset = DataSet()
dataset.add_data(10)
dataset.add_data(30)
dataset.add_data("string")
dataset.get_data()


'''Challenge
Create a class MLModel with private attributes __name and __accuracy. 
Add a getter for both. 
Add a train(accuracy) method that sets accuracy only if it's between 0 and 100, 
otherwise prints a warning.'''

class MLModel:

    def __init__(self, name):
        self.__name = name
        self.__accuracy = 0.0

    def get_name(self):
        return self.__name
    
    def get_accuracy(self):
        return self.__accuracy
    
    def train(self, accuracy):
        if accuracy > 0 and accuracy < 100:
            self.__accuracy = accuracy
            print(f"{self.__name} trained! Accuracy: {self.__accuracy}%")
        else:
            print(f"Warning!\n'{accuracy}' is not b/w 0 and 100")
        

model = MLModel("RandomForest")
print(model.get_accuracy())    
model.train(92.5)              
print(model.get_accuracy())   
model.train(150)               