# Your manager just gave you the Titanic dataset and said:
# "Before we do anything — inspect this dataset completely
#  and give me a full report"
#
# Task:
# 1. Load the dataset
# 2. Print total rows and columns
# 3. Print all column names and their data types
# 4. Print full df.info() summary
# 5. Print missing values count for every column
# 6. Print missing values as PERCENTAGE of total rows
#    hint: (df.isnull().sum() / len(df)) * 100
# 7. Print which columns have MORE than 20% missing values
# 8. Print a summary like this:
#
# ════════════════════════════════════
#      DATASET INSPECTION REPORT
# ════════════════════════════════════
# Total Rows    : 891
# Total Columns : 12
#
# Missing Values:
# Age      : 177 missing (19.87%)
# Cabin    : 687 missing (77.10%)  ← needs attention!
# Embarked : 2 missing (0.22%)
#
# Columns with >20% missing:
# Cabin : 77.10% missing
# ════════════════════════════════════


import pandas as pd

#Load data
df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

#total rows and column
row, column = df.shape

print(f"Total Rows: {row}")
print(f"Total Columns: {column}")

#column names and data types
print(f"{'Column Name':<15} {'Data Type'}")

for col,dtype in zip(df.columns,df.dtypes):
    print(f"{col:<15}: {dtype}")

#summary
df.info()

#missing values and percentage of every column
print("Missing Values:")
total_rows = len(df)
for col in df.columns:
    missing_values_count = df[col].isnull().sum()
    percentage_of_missing_values = ((missing_values_count / total_rows) * 100).round(2)
    print(f"{col:<15}:{missing_values_count} missing ({percentage_of_missing_values}%)")


#columns MORE than 20% missing values
print("\nColumns with >20% missing:")
for col in df.columns:
    missing_values_count = df[col].isnull().sum()
    percentage_of_missing_values = ((missing_values_count / total_rows) * 100).round(2)

    if percentage_of_missing_values > 20:
        print(f"{col:<15}: {percentage_of_missing_values}% missing")




# Your manager says:
# "The data types look wrong in some columns
#  fix them before analysis"
#
# Task:
# 1. Print current dtypes of all columns
# 2. Convert Pclass from int to string
#    because it represents a category not a number
# 3. Convert PassengerId from int to string
#    because it's an ID not a number
# 4. Add a new column 'Fare_int' — Fare converted to int
#    (removes decimal points)
# 5. Print dtypes again to confirm changes
# 6. Print this comparison:
#    Before: Pclass is int64
#    After:  Pclass is object

import pandas as pd

#Load data
df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print("BEFORE")
print(df.dtypes)

pclass_before = df["Pclass"].dtypes

df["Pclass"] = df["Pclass"].astype(str)

df["PassengerId"] = df["PassengerId"].astype(str)

df["Fare_int"] = df["Fare"].astype(int)

print("AFTER")
print(df.dtypes)

print(f"Before: Pclass is {pclass_before}")

print(f"After: Pclass is {df["Pclass"].dtypes}")


# Your manager says:
# "Clean all missing values using proper strategies
#  explain why you chose each strategy"
#
# Task:
# 1. Age column — fill with MEDIAN
#    why? because Age has outliers
#    print mean and median of Age before filling
#    fill missing Ages with median
#    confirm 0 missing values after filling
#
# 2. Embarked column — fill with MODE
#    why? because it is categorical
#    print mode of Embarked before filling
#    fill missing Embarked with mode
#    confirm 0 missing values after filling
#
# 3. Cabin column — fill with "Unknown"
#    why? because 77% missing — too much to guess
#    fill missing Cabin with "Unknown"
#    confirm 0 missing values after filling
#
# 4. Print final missing values count — should be all zeros!
#
# 5. Print explanation like:
#    Age     → filled with median (29.0) — has outliers
#    Embarked → filled with mode (S) — categorical column
#    Cabin    → filled with Unknown — 77% missing, can't guess


import pandas as pd

#Load data
df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

# calculate values before filling
age_median = df["Age"].median()
embarked_mode = df["Embarked"].mode()[0]
cabin_missing_pct = (df["Cabin"].isnull().sum() / len(df)) * 100

print("Before Filling Age Column")
print(df["Age"].agg(["mean","median"]).round(2))

print("After Filling Age Column")
df["Age"] = df["Age"].fillna(df["Age"].median()).round(2)
print(df["Age"].isnull().sum())


print("Before Filling Embarked Column")
print(df["Embarked"].mode())

print("After Filling Embarked Column")
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df["Embarked"].isnull().sum())

total_rows = len(df)
cabin_null_values = ((df["Cabin"].isnull().sum()/total_rows) * 100)
print(f"Percentage of cabin: {cabin_null_values}")

df["Cabin"] = df["Cabin"].fillna("Unknown")
print(df["Cabin"].isnull().sum())

print("FINAL MISSING VALUES CHECK")
print(df.isnull().sum())
print("\n All missing values cleaned!")

#explanation
print("CLEANING STRATEGY EXPLANATION")
print(f"Age        filled with median ({age_median}) - has outliers")
print(f"Embarked   filled with mode ({embarked_mode}) - categorical column")
print(f"Cabin      filled with Unknown - {cabin_missing_pct:.2f}% missing, can't guess")


# Your manager says:
# "Someone entered the data inconsistently
#  standardize it before we share with the client"
#
# Task:
# 1. Create this messy DataFrame:
#
# data = {
#     "Name":   ["Ahmed", "Sara", "Ali", "Zara", "Usman"],
#     "Gender": ["Male", "female", "MALE", "Female", "male"],
#     "City":   ["karachi", "LAHORE", "Karachi", "lahore", "KARACHI"],
#     "Status": ["Active", "active", "ACTIVE", "inactive", "Inactive"]
# }
#
# 2. Standardize Gender column:
#    all variations of male   → "Male"
#    all variations of female → "Female"
#    hint: use replace() with a dictionary
#
# 3. Standardize City column:
#    all variations → proper Title Case
#    hint: df["City"].str.title()
#
# 4. Standardize Status column:
#    all variations of active   → "Active"
#    all variations of inactive → "Inactive"
#
# 5. Print before and after for each column


import pandas as pd

data = {
    "Name":   ["Ahmed", "Sara", "Ali", "Zara", "Usman"],
    "Gender": ["Male", "female", "MALE", "Female", "male"],
    "City":   ["karachi", "LAHORE", "Karachi", "lahore", "KARACHI"],
    "Status": ["Active", "active", "ACTIVE", "inactive", "Inactive"]
}
df = pd.DataFrame(data)

print("Before Standardizing:")
print(df["Gender"])
df["Gender"] = df["Gender"].str.lower().replace({
    "male": "Male",
    "female": "Female"
})
print("After Standardizing:")
print(df["Gender"])

print("Before Standardizing:")
print(df["City"])
df["City"] = df["City"].str.title()
print("After Standardizing:")
print(df["City"])

print("Before Standardizing:")
print(df["Status"])
df["Status"] = df["Status"].str.lower().replace({
    "inactive": "Inactive",
    "active": "Active"
})
print("After Standardizing:")
print(df["Status"])


# Your manager says:
# "For each scenario below decide whether to use
#  dropna() or fillna() and apply it"
#
# Scenario 1:
# A survey dataset has 1000 rows
# Only 5 rows have missing Age values
# → Use dropna() — why? only 0.5% data loss
# → Apply dropna(subset=["Age"])
# → Print rows before and after
#
# Scenario 2:
# Same dataset but 400 rows have missing Income values
# → Use fillna() — why? dropping 40% data is too much!
# → Fill with median Income
# → Print before and after
#
# Create a sample DataFrame to demonstrate both:
# data = {
#     "Name":   ["Ahmed","Sara","Ali","Zara","Usman","Bilal","Hira"],
#     "Age":    [20, None, 21, 20, None, 22, 19],
#     "Income": [50000, 60000, None, None, None, 70000, None]
# }


import pandas as pd
data = {
    "Name":   ["Ahmed","Sara","Ali","Zara","Usman","Bilal","Hira"],
    "Age":    [20, None, 21, 20, None, 22, 19],
    "Income": [50000, 60000, None, None, None, 70000, None]
}
df = pd.DataFrame(data)

print("Before")
print(f"{len(df)} rows")
print(df)

print("After Dropping")
df = df.dropna(subset=["Age"])
print(f"{len(df)} rows")
print(df)


import pandas as pd
data = {
    "Name":   ["Ahmed","Sara","Ali","Zara","Usman","Bilal","Hira"],
    "Age":    [20, None, 21, 20, None, 22, 19],
    "Income": [50000, 60000, None, None, None, 70000, None]
}
df = pd.DataFrame(data)
print("Before")
print(f"{len(df)} rows")
print(df)

print("After Filling")
df["Income"] = df["Income"].fillna(df["Income"].median()).round(2)
print(f"{len(df)} rows")
print(df)


# Your manager says:
# "I need you to understand the difference between
#  map() and replace() — demonstrate both"
#
# Using Titanic dataset:
#
# 1. Using map() — convert Sex to numeric:
#    male   → 0
#    female → 1
#    Store in 'Sex_map'
#    Print result
#    What happens to unmatched values? → NaN
#
# 2. Using replace() — convert Sex to numeric:
#    male   → 0
#    female → 1
#    Store in 'Sex_replace'
#    Print result
#
# 3. Now test the difference:
#    Add "unknown" to some rows and see what happens
#    with map() vs replace()
#
# 4. Print the difference:
#    map()     → unmatched values become NaN
#    replace() → unmatched values stay unchanged


import pandas as pd

#Load data
df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

df["Sex_map"] = df["Sex"].map({
    "male": 0,
    "female": 1
})
print(df["Sex_map"])

df["Sex_replace"] =  df["Sex"].replace({
    "male": 1,
    "female": 0
})
print(df["Sex_replace"])


df.loc[0,"Sex"] = "unknown"
df.loc[5,"Sex"] = "unknown"
df.loc[10,"Sex"] = "unknown"

#using map
df["Sex_map"] = df["Sex"].map({
    "male": 0,
    "female": 1
})

#using replace
df["Sex_replace"] =  df["Sex"].replace({
    "male": 1,
    "female": 0
})

print(df[["Sex","Sex_map","Sex_replace"]].head(15))
