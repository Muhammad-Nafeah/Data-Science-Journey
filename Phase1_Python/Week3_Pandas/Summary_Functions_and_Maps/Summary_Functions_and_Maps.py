# axis=0  → Apply function to each COLUMN (default)
# axis=1  → Apply function to each ROW

# 1. map()
# map() works on one Series (one column).

# 2. apply()
# apply() is more powerful than map().

# It can work on:
# A Series (one column)
# A whole row
# A whole DataFrame

# Syntax:

# df.apply(function, axis=0(by default))


# 4. idxmax() ⭐

# idxmax() returns the index label of the maximum value, not the maximum value itself.

# 5. idxmin()

# Works exactly the same way.


# Using Titanic dataset:
# 1. Print full describe() for ALL columns including non-numeric
#    hint: df.describe(include='all')
# 2. Print mean age of all passengers
# 3. Print median fare paid
# 4. Print the most expensive fare paid and who paid it
#    hint: use idxmax() to find the row
# 5. Print the youngest passenger and their details
#    hint: use idxmin()
# 6. Print the oldest passenger and their details
# 7. How many unique passenger classes exist?
# 8. How many unique embarkation ports exist?

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print(df.describe(include='all'))

print(f"Mean Age: {df['Age'].mean():.2f}")
print(f"Median Fare: ${df['Fare'].median():.2f}")

most_expensive_fare = df["Fare"].idxmax()
who_paid = df.loc[most_expensive_fare,"Name"]
print(who_paid)

youngest_passenger = df["Age"].idxmin()
youngest_passenger_details = df.loc[youngest_passenger]
print(youngest_passenger_details)

oldest_passenger = df["Age"].idxmax()
oldest_passenger_detail = df.loc[oldest_passenger]
print(oldest_passenger_detail)

unique_classes = df["Pclass"].nunique()
print(f"Unique Passenger Classes: {unique_classes}")

unique_port = df["Embarked"].nunique()
print(f"Unique Embarkation Ports: {unique_port}")


# Using Titanic dataset:
# 1. How many males and females were on board?
#    use value_counts()
# 2. How many passengers in each class?
#    show as percentages too — value_counts(normalize=True)
# 3. How many passengers boarded from each port?
# 4. How many passengers survived vs died?
#    show both count and percentage
# 5. What were the top 10 most common passenger names?
#    hint: value_counts().head(10)


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

males_females = df["Sex"].value_counts()
print(males_females)

count = df["Pclass"].value_counts()
percentage = (df["Pclass"].value_counts(normalize=True) * 100).round(2)
print("Count:")
print(count)
print("Percentage:")
print(percentage)

passenger_boarded = df["Embarked"].value_counts()
print(passenger_boarded)

survived_vs_died = df["Survived"].value_counts()
print(survived_vs_died)

survived_vs_died_percentage = (df["Survived"].value_counts(normalize=True) * 100).round(2)
print(survived_vs_died_percentage)

top_10_common_names = (df["Name"].value_counts()).head(10)
print(top_10_common_names)


# Using Titanic dataset:
# 1. What was the average age of males vs females?
# 2. What was the average fare in each passenger class?
# 3. What was the survival rate for each gender?
#    hint: mean() on Survived column gives survival rate
# 4. What was the average age in each passenger class?
# 5. Who had higher median fare — survivors or non survivors?


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

male = df[df["Sex"] == "male"]
male_average_age = male["Age"].mean()
print(male_average_age)

female = df[df["Sex"] == "female"]
female_average_age = female["Age"].mean()
print(female_average_age)

first_class = df[df["Pclass"] == 1]
second_class = df[df["Pclass"] == 2]
third_class = df[df["Pclass"] == 3]

average_fare_1 = first_class["Fare"].mean()
print(average_fare_1)
average_fare_2 = second_class["Fare"].mean()
print(average_fare_2)
average_fare_3 = third_class["Fare"].mean()
print(average_fare_3)

male = df[df["Sex"] == "male"]
female = df[df["Sex"] == "female"]

male_survival_rate = male["Survived"].mean()
print(male_survival_rate)
female_survival_rate = female["Survived"].mean()
print(female_survival_rate)

first_class = df[df["Pclass"] == 1]
second_class = df[df["Pclass"] == 2]
third_class = df[df["Pclass"] == 3]

average_age_1 = first_class["Age"].mean()
print(average_age_1)
average_age_2 = second_class["Age"].mean()
print(average_age_2)
average_age_3 = third_class["Age"].mean()
print(average_age_3)


survivors = df[df["Survived"] == 1]
non_survivors = df[df["Survived"] != 1]

survivors_fare = survivors["Fare"].median()
non_survivors_fare = non_survivors["Fare"].median()
if survivors_fare > non_survivors_fare:
    print("Survivors had the higher median fare.")
else:
    print("Non-survivors had the higher median fare.")


# Using Titanic dataset:
# 1. Map 'Sex' column:
#    'male'   → 0
#    'female' → 1
#    Store in new column 'Sex_Numeric'
#
# 2. Map 'Survived' column:
#    0 → 'Died'
#    1 → 'Survived'
#    Store in new column 'Survival_Status'
#
# 3. Map 'Pclass' column:
#    1 → 'First Class'
#    2 → 'Second Class'
#    3 → 'Third Class'
#    Store in new column 'Class_Name'
#
# 4. Print first 10 rows showing:
#    Name, Sex_Numeric, Survival_Status, Class_Name

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

df["Sex_Numeric"] = df["Sex"].map({
    'male': 0,
    'female': 1
})
print(df["Sex_Numeric"])


df["Survival_Status"] = df["Survived"].map({
    0:'Died',
    1:'Survived'
})
print(df["Survival_Status"])

df["Class_Name"] = df["Pclass"].map({
    1:'First Class',
    2:'Second Class',
    3:'Third Class'
})
print(df["Class_Name"])

print(df[["Name","Sex_Numeric","Survival_Status","Class_Name"]].head(10))


# Using Titanic dataset:
# Create a function called categorize_age:
#    Age < 13        → 'Child'
#    13 <= Age < 18  → 'Teenager'
#    18 <= Age < 60  → 'Adult'
#    Age >= 60       → 'Senior'
#    Age is NaN      → 'Unknown'
#
# Apply it using map() to create 'Age_Group' column
# Print value_counts() of Age_Group
# Print survival rate for each Age_Group
#    hint: groupby Age_Group then mean() on Survived

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

def categorize_age(age):

    if pd.isnull(age):
        return 'Unknown'
    elif age < 13:
        return 'Child'
    elif age >= 13 and age < 18:
        return 'Teenager'
    elif age >= 18 and age < 60:
        return 'Adult'
    else:
        return 'Senior'
    
df["Age_Group"] = df["Age"].map(categorize_age)
print(df["Age_Group"])

print(df["Age_Group"].value_counts())

age_group_1 = df[df["Age_Group"] == 'Unknown']
age_group_2 = df[df["Age_Group"] == 'Child']
age_group_3 = df[df["Age_Group"] == 'Teenager']
age_group_4 = df[df["Age_Group"] == 'Adult']
age_group_5 = df[df["Age_Group"] == 'Senior']

survival_rate_1 = age_group_1["Survived"].mean()
print(f"{survival_rate_1:.2f}")
survival_rate_2 = age_group_2["Survived"].mean()
print(f"{survival_rate_2:.2f}")
survival_rate_3 = age_group_3["Survived"].mean()
print(f"{survival_rate_3:.2f}")
survival_rate_4 = age_group_4["Survived"].mean()
print(f"{survival_rate_4:.2f}")
survival_rate_5 = age_group_5["Survived"].mean()
print(f"{survival_rate_5:.2f}")


# Using Titanic dataset:
# 1. Create a function called get_title that extracts
#    title from passenger name:
#    "Braund, Mr. Owen Harris"  → "Mr"
#    "Heikkinen, Miss. Laina"   → "Miss"
#    hint: use split() and strip()
#
# 2. Apply it to Name column to create 'Title' column
#
# 3. Print value_counts() of Title column
#    Expected: Mr, Miss, Mrs, Master are most common
#
# 4. Print survival rate for each Title


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

def get_title(name):

    title = name.split(",")[1].split(".")[0].strip()
    return title

df["Title"] = df["Name"].apply(get_title)
print(df["Title"].value_counts())

titles = df["Title"].unique()

for title in titles:
    title_df = df[df["Title"] == title]

    survival_rate = (title_df["Survived"].mean() * 100)

    count = len(title_df)

    print(f"{title:15} {survival_rate:.2f}% ({count} passengers)")


# Using Titanic dataset:
# Create a function called passenger_profile that takes a row
# and returns a description string like:
# "Mr. Ahmed — 25yr old Male, First Class, Survived"
# "Miss. Sara — 18yr old Female, Third Class, Did not survive"
#
# Apply it using df.apply(func, axis=1)
# Store in column 'Profile'
# Print first 10 profiles


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

df["Passenger_Class"] = df["Pclass"].map({
        1: "First Class",
        2: "Second Class",
        3: "Third Class"
    })
df["Survived_Passenger"] = df["Survived"].map({
        0: "Did not survive",
        1: "Survived"
    })
def passenger_profile(row):

    return f'{row["Name"]} - {row["Age"]}yr old {row["Sex"].title()}, {row["Passenger_Class"]}, {row["Survived_Passenger"]}'

df["Profile"] = df.apply(passenger_profile,axis=1)
print(df["Profile"].head(10))

# Using Titanic dataset:
# 1. Using lambda + map:
#    Create 'Fare_Rounded' — round fare to nearest 10
#    hint: lambda x: round(x/10)*10
#
# 2. Using lambda + apply:
#    Create 'Name_Length' — number of characters in name
#
# 3. Using lambda + apply:
#    Create 'Is_Alone' — True if SibSp + Parch == 0
#
# 4. Using lambda + apply with axis=1:
#    Create 'Survival_Chance':
#    'High'   if female and First Class
#    'Medium' if female and not First Class
#    'Medium' if male and First Class
#    'Low'    if male and not First Class
#
# 5. Print value_counts() of Survival_Chance
# 6. Print actual survival rate for each Survival_Chance category


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

df["Fare_Rounded"] = df["Fare"].map(lambda x: round(x / 10) * 10)
print(df["Fare_Rounded"])

df["Name_Length"] = df["Name"].apply(len)
print(df["Name_Length"])


def func(row):
    # if row["SibSp"] + row["Parch"] == 0:
    #     return True
    # else:
    #     return False
    return row["SibSp"] + row["Parch"] == 0
    
df["Is_Alone"] = df.apply(func,axis=1)
print(df["Is_Alone"])


df["Passenger_Class"] = df["Pclass"].map({
        1: "First Class",
        2: "Second Class",
        3: "Third Class"
    })
def survival_chance(row):
    if (row["Sex"] == "female") and (row["Passenger_Class"] == "First Class"):
        return 'High'
    elif (row["Sex"] == "female") and (row["Passenger_Class"] != "First Class"):
        return 'Medium'
    elif (row["Sex"] == "male") and (row["Passenger_Class"] == "First Class"):
        return 'Medium'
    else:
        return 'Low'
    
df["Survival_Chance"] = df.apply(survival_chance,axis=1)
print(df["Survival_Chance"].value_counts())

survival_category = df["Survival_Chance"].unique()

for surviver in survival_category:

    survival_df = df[df["Survival_Chance"] == surviver]

    survival_rate = (survival_df["Survived"].mean() * 100)

    count = len(survival_df)

    print(f"{surviver:15} {survival_rate:.2f}% ({count} passengers)")

# Titanic Survival Report
# Write a function called titanic_report(df) that prints:
#
# ═══════════════════════════════════
#      TITANIC SURVIVAL REPORT
# ═══════════════════════════════════
# Total Passengers : 891
# Total Survived   : 342 (38.38%)
# Total Died       : 549 (61.62%)
#
# ── BY GENDER ──────────────────────
# Female Survival Rate : 74.20%
# Male Survival Rate   : 18.89%
#
# ── BY CLASS ───────────────────────
# First Class  Survival Rate : 62.96%
# Second Class Survival Rate : 47.28%
# Third Class  Survival Rate : 24.24%
#
# ── BY AGE GROUP ───────────────────
# Child    Survival Rate : XX.XX%
# Teenager Survival Rate : XX.XX%
# Adult    Survival Rate : XX.XX%
# Senior   Survival Rate : XX.XX%
#
# ── TOP INSIGHT ────────────────────
# Highest Fare Paid : $512.33 by [Name]
# Youngest Survivor : X years old
# Oldest Survivor   : XX years old
# ═══════════════════════════════════

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

def titanic_report(df):

    total_passengers = len(df)
    total_survived = df[df["Survived"] == 1]
    total_died = df[df["Survived"] != 1]
    survived_pct = (len(total_survived) / total_passengers) * 100
    died_pct = (len(total_died) / total_passengers) * 100

    female = df[df["Sex"] == "female"]
    female_survival_rate = (female["Survived"].mean() * 100)

    male = df[df["Sex"] == "male"]
    male_survival_rate = (male["Survived"].mean() * 100)

    first_class = df[df["Pclass"] == 1]
    first_class_survival_rate = (first_class["Survived"].mean() * 100)

    second_class = df[df["Pclass"] == 2]
    second_class_survival_rate = (second_class["Survived"].mean() * 100)

    third_class = df[df["Pclass"] == 3]
    third_class_survival_rate = (third_class["Survived"].mean() * 100)

    def categorize_age(age):
        if pd.isnull(age):
            return 'Unknown'
        elif age < 13:
            return 'Child'
        elif age >= 13 and age < 18:
            return 'Teenager'
        elif age >= 18 and age < 60:
            return 'Adult'
        else:
            return 'Senior'

    df["Age_Group"] = df["Age"].map(categorize_age)

    age_group_1 = df[df["Age_Group"] == 'Unknown']
    age_group_2 = df[df["Age_Group"] == 'Child']
    age_group_3 = df[df["Age_Group"] == 'Teenager']
    age_group_4 = df[df["Age_Group"] == 'Adult']
    age_group_5 = df[df["Age_Group"] == 'Senior']

    survival_rate_1 = (age_group_1["Survived"].mean() * 100)
    survival_rate_2 = (age_group_2["Survived"].mean() * 100)
    survival_rate_3 = (age_group_3["Survived"].mean() * 100)
    survival_rate_4 = (age_group_4["Survived"].mean() * 100)
    survival_rate_5 = (age_group_5["Survived"].mean() * 100)

    fare = df["Fare"].idxmax()
    who_paid = df.loc[fare, "Name"]
    highest_fare = df.loc[fare, "Fare"]

    survivors = df[df["Survived"] == 1]
    youngest_survivor = survivors["Age"].idxmin()
    youngest_age = df.loc[youngest_survivor, "Age"]

    oldest_survivor = survivors["Age"].idxmax()
    oldest_age = df.loc[oldest_survivor, "Age"]

    # printing
    print("="*35)
    print("      TITANIC SURVIVAL REPORT      ")
    print("="*35)
    print(f"Total Passengers : {total_passengers}")
    print(f"Total Survived   : {len(total_survived)} ({survived_pct:.2f}%)")
    print(f"Total Died       : {len(total_died)} ({died_pct:.2f}%)")

    print("\n-- BY GENDER ----------------------")
    print(f"Female Survival Rate : {female_survival_rate:.2f}%")
    print(f"Male Survival Rate   : {male_survival_rate:.2f}%")

    print("\n-- BY CLASS  ----------------------")
    print(f"First Class  Survival Rate : {first_class_survival_rate:.2f}%")
    print(f"Second Class Survival Rate : {second_class_survival_rate:.2f}%")
    print(f"Third Class  Survival Rate : {third_class_survival_rate:.2f}%")

    print("\n-- BY AGE GROUP -------------------")
    print(f"Unknown  Survival Rate : {survival_rate_1:.2f}%")
    print(f"Child    Survival Rate : {survival_rate_2:.2f}%")
    print(f"Teenager Survival Rate : {survival_rate_3:.2f}%")
    print(f"Adult    Survival Rate : {survival_rate_4:.2f}%")
    print(f"Senior   Survival Rate : {survival_rate_5:.2f}%")

    print("\n-- TOP INSIGHT --------------------")
    print(f"Highest Fare Paid : ${highest_fare:.2f} by {who_paid}")
    print(f"Youngest Survivor : {youngest_age:.0f} years old")
    print(f"Oldest Survivor   : {oldest_age:.0f} years old")
    print("="*35)

titanic_report(df)










