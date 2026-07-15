# Exercise 1: Create a Series

# Create a Series named marks with:

# Ali      85
# Ahmed    90
# Sara     95

# The Series name should be:

# Exam Results

import pandas as pd

marks = pd.Series([85,90,95],index=['Ali','Ahmed','Sara'], name="Exam Results")
print(marks)


# Exercise 2: Create a DataFrame

# Create a DataFrame named students:

# Name	Age
# Ali	20
# Ahmed	21
# Sara	22

students = pd.DataFrame({'Name':['Ali','Ahmed','Sara'],'Age':[20,21,22]})
print(students)

# Exercise 3: Custom Index

# Create the same DataFrame as Exercise 2 but use:

# S1
# S2
# S3

# as the index.

students = pd.DataFrame({'Name':['Ali','Ahmed','Sara'],'Age':[20,21,22]},index=['S1','S2','S3'])
print(students)


# Exercise 4: Products Table

# Create this DataFrame:

# Product	Price
# Laptop	80000
# Mouse	    2000
# Keyboard	5000

# Store it in a variable called products.


products = pd.DataFrame({'Product':['Laptop','Mouse','Keyboard'],'Price':[8000,2000,5000]})
print(products)


# Exercise 5: Monthly Sales

# Create this DataFrame:

# 	Sales
# January	100
# February	120
# March	    150

# The row labels must be:
# January
# February
# March

sales = pd.DataFrame({'Sales':[100,120,150]},index=['January','February','March'])
print(sales)


# Exercise 6: Create a Series

# Create a Series called cities:

# Karachi
# Lahore
# Islamabad
# Peshawar

# Give it the name:

# Pakistan Cities

cities = pd.Series(['Karachi','Lahore','Islamabad','Peshawar'],name="Pakistan Cities")
print(cities)


# Exercise 7: DataFrame Shape

# Create:

employees = pd.DataFrame({
    "Name": ["Ali", "Ahmed", "Sara", "Ayesha"],"Salary": [50000, 60000, 70000, 80000]
})

# Without running the code:

# Question:

# What will be the output of:

print(employees.shape)
#(4,2)

# Exercise 8: Read a CSV

# Write only the code needed to read:

# students.csv

# into a DataFrame called students.

students = pd.read_csv("students.csv")


# Exercise 9: Save a CSV

# Suppose you have:

df = pd.DataFrame(...)

# Write the code to save it as:

# employee_data.csv

df.to_csv("employee_data.csv")



# Exercise 10 (Challenge)

# Create this DataFrame exactly:

#            Math  English  Science
# Student A   85      78       90
# Student B   92      88       84
# Student C   75      80       89

# Variable name:

# results

results = pd.DataFrame({'Math':[85,92,75],'English':[78,88,80],'Science':[90,84,89]},index=['Student A','Student B','Student C'])
print(results)

# Create a DataFrame of 5 Pakistani cities with:
# columns: City, Province, Population (millions), Area (km2)
# Data:
# Karachi, Sindh, 16.1, 3527
# Lahore, Punjab, 13.1, 1772
# Islamabad, ICT, 1.1, 906
# Peshawar, KPK, 2.0, 1257
# Quetta, Balochistan, 1.2, 2653
#
# Print the DataFrame
# Print its shape
# Print its columns
# Print its dtypes


df =  pd.DataFrame({'City':['Karachi','Lahore','Islamabad','Peshawar','Quetta'],
                    'Province':['Sindh','Punjab','ICT','KPK','Balochistan'],
                    'Population (millions)':[16.1, 13.1, 1.1, 2.0, 1.2],
                    'Area (km2)':[3517, 1772, 906, 1257,2653]})
print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)

# Create a DataFrame of 5 students using separate lists:
# names =    ["Ahmed", "Sara", "Ali", "Zara", "Usman"]
# ages =     [20, 19, 21, 20, 22]
# grades =   ["A", "B", "A", "C", "B"]
# marks =    [92, 78, 88, 65, 81]
#
# Print first 3 rows using head()
# Print last 2 rows using tail()
# Print basic info using info()
# Print statistics using describe()


names =    ["Ahmed", "Sara", "Ali", "Zara", "Usman"]
ages =     [20, 19, 21, 20, 22]
grades =   ["A", "B", "A", "C", "B"]
marks =    [92, 78, 88, 65, 81]

df = pd.DataFrame({'Name': names, 'Age':ages, 'Grade':grades, 'Marks':marks})

print(df.head(3))
print(df.tail(2))
print(df.info())
print(df.describe())



# Read dataset with pd.read_csv()
# Print first 5 rows
# Print shape — how many rows and columns
# Print all column names
# Print data types of each column
# Print how many missing values in each column


df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.isnull().sum())



# Take your cities DataFrame from Q1
# Save it to a CSV file called "pakistani_cities.csv"
# Read it back and print it to confirm it saved correctly
# Save it again without the index column
# (hint: use index=False)


df =  pd.DataFrame({'City':['Karachi','Lahore','Islamabad','Peshawar','Quetta'],
                    'Province':['Sindh','Punjab','ICT','KPK','Balochistan'],
                    'Population (millions)':[16.1, 13.1, 1.1, 2.0, 1.2],
                    'Area (km2)':[3517, 1772, 906, 1257,2653]})
df.to_csv("Phase1_Python/Week3_Pandas/datasets/pakistani_cities.csv",index=False)
print("File saved successfully!")

df_check = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/pakistani_cities.csv")
print("\nFile read back successfully!")
print(df_check)



# Create this DataFrame:
# students = {
#     "Name":    ["Ahmed", "Sara", "Ali", "Zara", "Usman"],
#     "Math":    [88, 72, 95, 60, 78],
#     "English": [75, 90, 68, 85, 92],
#     "Science": [92, 85, 78, 70, 88],
#     "Urdu":    [80, 77, 88, 95, 72]
# }
#
# 1. Print the full DataFrame
# 2. Print shape — rows and columns
# 3. Print dtypes of each column
# 4. Print summary statistics using describe()
# 5. Save to "student_report.csv" without index
# 6. Read it back and confirm


import pandas as pd
df = pd.DataFrame(
    {
    "Name":    ["Ahmed", "Sara", "Ali", "Zara", "Usman"],
    "Math":    [88, 72, 95, 60, 78],
    "English": [75, 90, 68, 85, 92],
    "Science": [92, 85, 78, 70, 88],
    "Urdu":    [80, 77, 88, 95, 72]
}
)

print(df)
print(df.shape)
print(df.dtypes)
print(df.describe())

df.to_csv("Phase1_Python/Week3_Pandas/datasets/student_report.csv",index=False)
print("File saved successfully!")

df_check = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/student_report.csv")
print("\nFile read back successfully!")
print(df_check)


