'''Basic
Create 3 classes Car, Boat, Plane — each has a method fuel_type() 
that prints what fuel it uses. Put all 3 in a list and loop through 
calling fuel_type().'''

class Car:
    def fuel_type(self):
        print("Using Petrol.....")
class Boat:
    def fuel_type(self):
        print("Using Diesel.....")
class Plane:
    def fuel_type(self):
        print("Using Gas......")

vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    vehicle.fuel_type()


'''DS Theme
Create 3 classes LinearRegression, DecisionTree, KNN — each has a method predict() 
that prints how that model makes predictions. Loop through all 3.
LinearRegression → "Predicting using a straight line..."
DecisionTree     → "Predicting using if/else tree rules..."
KNN              → "Predicting using nearest neighbors..."'''

class LinearRegression:
    def predict(self):
        print("Predicting using a straight line...")

class DecisionTree:
    def predict(self):
        print("Predicting using if/else tree rules...")  
class KNN:
    def predict(self):
        print("Predicting using nearest neighbors...") 

models = [LinearRegression(), DecisionTree(), KNN()]
for model in models:
    model.predict()


'''Challenge
Create a base class DataProcessor with two methods 
clean() and transform(). Create two child classes:

CSVProcessor — overrides both methods for CSV data
JSONProcessor — overrides both methods for JSON data

Loop through both and call both methods.'''
     

class DataProcessor():
    def clean(self):
        pass
    def transform(self):
        pass

class CSVProcessor(DataProcessor):
    def clean(self):
        print("Cleaning CSV data...")
    def transform(self):
        print("Transforming CSV into DataFrame... ")

class JSONProcessor(DataProcessor):
    def clean(self):
        print("Cleaning JSON data...")
    def transform(self):
        print("Transforming JSON into dictionary... ")

processors = [CSVProcessor(), JSONProcessor()]
for processor in processors:
    processor.clean()
    processor.transform()
