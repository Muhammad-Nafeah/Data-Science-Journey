'''Basic
Create an abstract class Animal with abstract method speak().
Create 3 child classes Dog, Cat, Duck — each implements speak().
Loop through all 3.'''


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

class Duck(Animal):
    def speak(self):
        print("Duck says: Quack!")
    
animals = [Dog(), Cat(), Duck()]
for animal in animals:
    animal.speak()


'''  DS Theme
Create an abstract class Visualization with abstract methods plot() and save().
Create two child classes BarChart and LineChart — each implements both methods.
Loop through both.'''

class Visualization(ABC):

    @abstractmethod
    def plot(self):
        print("Preparing canvas...")
    
    @abstractmethod
    def save(self):
        print("Saving canvas...")

class BarChart(Visualization):

    def plot(self):
        super().plot() #super() run parent plot() first 
        print("Plotting Bar Chart... ")
    def save(self):
        super().save()   #super() run parent save() first
        print("Saving Bar Chart as PNG... ")

class LineChart(Visualization):

    def plot(self):
        super().plot() #super() run parent plot() first
        print("Plotting Line Chart... ")
    def save(self):
        super().save() #super() run parent save() first
        print("Saving Line Chart as PNG... ")

visualizations = [BarChart(), LineChart()]
for visualizaion in visualizations:
    visualizaion.plot()
    visualizaion.save()
    

''' Challenge
Create an abstract class DatabaseConnector with 
abstract methods connect(), fetch_data(), and close().
Create two child classes MySQLConnector and MongoDBConnector 
— each implements all 3 methods.
Loop through both and call all 3 methods.'''


class DatabaseConnector(ABC):

    @abstractmethod
    def connect(self):
        print("Starting Connection....")
    
    @abstractmethod
    def fetch_data(self):
        print("Fetching Data.....")
    
    @abstractmethod
    def close(self):
        print("Connection Closed.....")


class MySQLConnector(DatabaseConnector):
    def connect(self):
        super().connect()                        # parent runs first
        print("MySQL connected on port 3306")  # then own code

    def fetch_data(self):
        super().fetch_data()
        print("Fetching MySQL tables...")

    def close(self):
        super().close()
        print("MySQL connection closed ")


class MongoDBConnector(DatabaseConnector):
    def connect(self):
        super().connect()
        print("MongoDB connected on port 27017 ")

    def fetch_data(self):
        super().fetch_data()
        print("Fetching MongoDB documents... ")

    def close(self):
        super().close()
        print("MongoDB connection closed ")
    
dbconnectors = [MySQLConnector(), MongoDBConnector()]
for dbconnector in dbconnectors:
    dbconnector.connect()
    dbconnector.fetch_data()
    dbconnector.close()



