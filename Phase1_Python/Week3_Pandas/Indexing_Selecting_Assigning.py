import pandas as pd
# Use the Titanic dataset
# 1. Select only the 'Name' column
# 2. Select only the 'Age' column
# 3. Select these 3 columns together:
#    ['Name', 'Age', 'Survived']
# 4. Print each result

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print(df["Name"])
print(df["Age"])

print(df[['Name', 'Age', 'Survived']])

# Using Titanic dataset and iloc:
# 1. Select the first row
# 2. Select the first 5 rows
# 3. Select the last 5 rows
# 4. Select rows 10 to 20
# 5. Select first 3 rows and first 3 columns
# 6. Select the Age column using iloc only
import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")
print(df.iloc[0])

print(df.head()) 
#or
print(df.iloc[0:5])

print(df.tail())
#or
print(df.iloc[-5:]) #Take rows from the 5th last row to the end.

print(df.iloc[10:21])

print(df.iloc[0:3,0:3])

print(df.iloc[:, 6])



# Using Titanic dataset and loc:
# 1. Select row with index 0
# 2. Select rows 0 to 10
# 3. Select rows 0 to 5, columns 'Name' and 'Age'
# 4. Select these columns only:
#    ['Name', 'Survived', 'Pclass', 'Age', 'Fare']

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print(df.loc[0])
print(df.loc[0:10])
print(df.loc[0:5,["Name","Age"]])
print(df.loc[:, ['Name', 'Survived', 'Pclass', 'Age', 'Fare']])


# Using Titanic dataset:
# 1. Select all passengers who Survived (Survived == 1)
# 2. Select all passengers who did NOT survive
# 3. Select all passengers in First Class (Pclass == 1)
# 4. Select all passengers older than 50
# 5. Print how many rows each result has


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

survived_passenger = df[df["Survived"] == 1]
not_survived_passenger = df[df["Survived"] != 1]
first_class_passenger = df[df["Pclass"] == 1]
older_than_50 = df[df["Age"] > 50]

print(len(survived_passenger))
print(len(not_survived_passenger))
print(len(first_class_passenger))
print(len(older_than_50))


# Using Titanic dataset:
# 1. Select passengers who Survived AND were in First Class
# 2. Select passengers who were female OR in First Class
# 3. Select male passengers older than 30 who survived
# 4. Select passengers whose fare was between 50 and 100
# 5. Print count of each result

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

survived_passenger = df[
    (df["Survived"] == 1) & 
    (df["Pclass"] == 1)
    ]
female_passenger = df[
    (df["Sex"] == "female") | 
    (df["Pclass"] == 1)
    ]
male_passenger = df[
    (df["Sex"] == "male") & 
    (df["Age"] > 30) & 
    (df["Survived"] == 1)
    ]
fare = df[
    (df["Fare"] > 50) & 
    (df["Fare"] < 100)
    ]

print(len(survived_passenger))
print(len(female_passenger))
print(len(male_passenger))
print(len(fare))

# Using Titanic dataset:
# 1. Select passengers who embarked from
#    'S' or 'C' using isin()
# 2. Select passengers where Age is missing
#    using isnull()
# 3. Select passengers where Age is NOT missing
#    using notnull()
# 4. Print count of missing ages
# 5. Print count of non missing ages

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

embarked = df[df["Embarked"].isin(['S','C'])]

missing_age = df[df["Age"].isnull()]
#or
#missing_age = df[df["Age"].isnull().sum()]


not_missing_age =  df[df["Age"].notnull()]
#or
#not_missing_age =  df[df["Age"].notnull().sum()]

#or
print(len(missing_age))
print(len(not_missing_age))

# Using Titanic dataset:
# 1. Add a new column called 'Family_Size'
#    Family_Size = SibSp + Parch + 1
#    (siblings + parents + the passenger themselves)
# 2. Add a column called 'Is_Child'
#    True if Age < 18, False otherwise
# 3. Add a column called 'Fare_Category'
#    'Low'    if Fare < 50
#    'Medium' if Fare between 50 and 100
#    'High'   if Fare > 100
# 4. Print first 10 rows showing new columns

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

df["Family_Size"] = df["SibSp"] + df["Parch"] + 1

df["Is_Child"] = df["Age"] < 18

def categorize_fare(fare):
    if fare < 50:
        return "Low"
    elif fare >= 50 and fare <= 100:
        return "Medium"
    else:
        return "High"
df["Fare_Category"] = df["Fare"].apply(categorize_fare)

print(df[["Family_Size", "Is_Child", "Fare_Category"]].head(10))
#or 
print(df.loc[0:9,["Family_Size", "Is_Child", "Fare_Category"]])

# Using Titanic dataset answer these questions:
# 1. How many women survived?
# 2. How many men survived?
# 3. How many children (age < 18) survived?
# 4. What percentage of First Class passengers survived?
# 5. Select all surviving women in First Class
#    and show only their Name, Age and Fare columns

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

# 1. Women survived
women_survived = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print(f"Women survived: {len(women_survived)}")

# 2. Men survived
men_survived = df[(df["Sex"] == "male") & (df["Survived"] == 1)]
print(f"Men survived: {len(men_survived)}") 

# 3. Children survived
children_survived = df[(df["Age"] < 18) & (df["Survived"] == 1)]
print(f"Children survived: {len(children_survived)}")

# 4. First class survival percentage
first_class = df[df["Pclass"] == 1]
first_class_survived = df[(df["Pclass"] == 1) & (df["Survived"] == 1)]
percentage = (len(first_class_survived) / len(first_class)) * 100 
print(f"First class survival: {percentage:.2f}%")

# 5. Surviving women in first class
women_first_class = df[
    (df["Sex"] == "female") &
    (df["Pclass"] == 1) &
    (df["Survived"] == 1)
]
print(women_first_class[["Name", "Age", "Fare"]])