#Basic Logic
#Create a class Book with attributes title, author, pages. Add a method summary() that prints all three neatly.

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"

book = Book('Harry Potter', 'J.K Rowling', 2000)
result = book.summary()
print(result)


# Method Logic
#Create a class BankAccount with attribute balance (starting at 0). Add methods deposit(amount) and withdraw(amount). Withdrawal should print a warning if balance is insufficient.

class BankAccount:

    def __init__(self):
        self.balance = 0
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposit Rs.{amount}. New Balance Rs.{self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print(f"Insufficient Balance! You only have Rs.{self.balance}")
        else:
            self.balance -= amount
            print(f"Withdraw Rs.{amount}. New Balance Rs.{self.balance}")

account = BankAccount()
account.deposit(120000)
account.withdraw(200000)


#Data Science Theme
#Create a class MLModel with attributes name and accuracy (default 0.0). Add a method train(new_accuracy) that updates the accuracy and prints "Model trained! Accuracy: X%".


class MLModel:

    def __init__(self, name):
        self.name = name
        self.accuracy = 0.0

    def train(self, new_accuracy):
        self.accuracy += new_accuracy
        print(f"Model Trained! Accuracy: {self.accuracy}%")

model = MLModel('Image Analysis')
model.train(45)


# Challenge
#Create a class Roadmap that stores your Data Science roadmap as a list of topics and tracks which ones are completed. Add methods complete_topic(topic) and progress() that prints how many topics are done out of total.

class Roadmap:

    def __init__(self):
        self.topics = ["Python", "OOP", "Bash", "NumPy", "SQL", "Statistics", "Pandas", "Visualization", "Projects"]
        self.completed = []

    def complete_topics(self, topic):

        if topic not in self.topics:
            print(f"{topic} is not in your roadmap.")
        elif topic in self.completed:
            print(f"{topic} is already completed!")
        else:
            self.completed.append(topic)
            print(f"Topics Completed: {self.completed}")
    
    def progress(self):
        print(f"{len(self.completed)} out of {len(self.topics)} topics completed!")

roadmap = Roadmap()
roadmap.complete_topics('Python')
roadmap.complete_topics('OOP')
roadmap.complete_topics('Python')
roadmap.complete_topics('DSA')
roadmap.complete_topics('Visualization')
roadmap.progress()

        


