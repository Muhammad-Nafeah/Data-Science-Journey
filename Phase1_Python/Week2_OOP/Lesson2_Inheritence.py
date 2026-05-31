# Basic Inheritance
# Create a class Animal with attribute name and method eat() that prints "{name} is eating." Then create a class Dog that inherits from Animal and adds a method bark() that prints "{name} says Woof!"

class Animal:

    def __init__(self,name):

        self.name = name
    
    def eat(self):

        print(f"{self.name} is eating. ")

class Dog(Animal):

    def bark(self):

        print(f"{self.name} says Woof!")

dog_sound = Dog("Dog")
dog_sound.eat()
dog_sound.bark()


# Using super()
# Create a class Vehicle with attributes brand and speed. Create a child class Car that adds an attribute doors using super(). Add a method describe() that prints all three attributes

class Vehicle:

    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):

    def __init__(self, brand, speed, doors):

        super().__init__(brand, speed)
        self.doors = doors

    def describe(self):
            
        print(f"Brand: {self.brand}\nSpeed: {self.speed}\nDoors: {self.doors}")

car = Car('Ferrari',10000,2)
car.describe()


# DS Theme
# Create a class Model with attributes name and method train() that prints "Training {name}..." Create two child classes LinearRegression and RandomForest — each adds its own attribute (degree for Linear, n_trees for RandomForest) and overrides train() to print something specific to that model.

class Model:

    def __init__(self, name):
        self.name = name 

    def train(self):

        print(f"Training {self.name}...")

class LinearRegression(Model):

    def __init__(self, name, degree):

        super().__init__(name)
        self.degree = degree

    def train(self):

        print(f"Training {self.name} with polynomial degree {self.degree}...")


class RandomForest(Model):
        
    def __init__(self, name, n_tree):

        super().__init__(name)
        self.n_tree = n_tree

    def train(self):

        print(f"Training {self.name} with {self.n_tree} decision trees...")

m = Model('model')
lr = LinearRegression('Linear Regression', 50)
rf = RandomForest('Random Forest', 100)

m.train()
lr.train()
rf.train()


