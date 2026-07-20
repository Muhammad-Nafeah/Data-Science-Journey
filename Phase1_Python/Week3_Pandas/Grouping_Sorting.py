# Using Titanic dataset:
# 1. Count total passengers by gender using size()
# 2. Count non-missing ages by gender using count()
# 3. Find average age by gender
# 4. Find average fare by passenger class
# 5. Find total fare collected from each class using sum()
# 6. Find survival rate by gender
# 7. Find survival rate by passenger class


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

total_passengers = df.groupby("Sex").size() #size counts missing values in the rows of groups.
print(total_passengers)

print(df.groupby("Sex")["Age"].count()) #count only counts non-missing values.

print(df.groupby("Sex")["Age"].mean().round(2))

print(df.groupby("Pclass")["Fare"].mean().round(2))

print(df.groupby("Pclass")["Fare"].sum().round(2))

print(df.groupby("Sex")["Survived"].mean().round(2) * 100)

print(df.groupby("Pclass")["Survived"].mean().round(2) * 100)



# Using Titanic dataset:
# 1. Find maximum fare paid in each class
# 2. Find minimum fare paid in each class
# 3. Find median age in each class
# 4. Find oldest passenger in each gender
# 5. Find youngest passenger in each gender

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print(df.groupby("Pclass")["Fare"].max())
print(df.groupby("Pclass")["Fare"].min())
print(df.groupby("Pclass")["Age"].median())
print(df.groupby("Sex")["Age"].max())
print(df.groupby("Sex")["Age"].min())


# Using Titanic dataset:
# 1. For each passenger class show:
#    mean, max, min, median of Fare — all in one line using agg()
#
# 2. For each gender show:
#    mean, max, min of Age — all in one line using agg()
#
# 3. For each embarkation port show:
#    count, mean of Survived — using agg()

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print(df.groupby("Pclass")["Fare"].agg(["mean","max","min"]))

print(df.groupby("Sex")["Age"].agg(["mean","max","min"]))

print(df.groupby("Embarked")["Survived"].agg(["count","mean"]))



# Using Titanic dataset:
# 1. Count passengers by Sex AND Pclass together
# 2. Find average fare by Sex AND Pclass together
# 3. Find survival rate by Sex AND Pclass together
#    (this is very interesting — print and observe!)
# 4. Find average age by Sex AND Survived together


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print(df.groupby(["Sex","Pclass"]).size())

print(df.groupby(["Sex","Pclass"])["Fare"].mean().round(2))

print((df.groupby(["Sex","Pclass"])["Survived"].mean() * 100).round(2))

print(df.groupby(["Sex","Survived"])["Age"].mean().round(2))


# Using Titanic dataset:
# 1. Sort passengers by Age — youngest first
# 2. Sort passengers by Age — oldest first
# 3. Sort passengers by Fare — most expensive first
#    show only Name, Pclass, Fare columns
# 4. Sort by Pclass first, then by Fare within each class
# 5. Sort passengers alphabetically by Name
# 6. Show top 5 highest paying passengers
#    Name, Pclass, Fare only


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print(df.sort_values("Age"))

print(df.sort_values("Age",ascending=False))

most_expensive_fare = df.sort_values("Fare",ascending=False)
print(most_expensive_fare[["Name","Pclass","Fare"]])

print(df.sort_values(["Pclass","Fare"]))

print(df.sort_values("Name"))

highest_paying_passengers = df.sort_values("Fare",ascending=False)
print(highest_paying_passengers[["Name","Pclass","Fare"]].head(5))


# Using Titanic dataset:
# 1. Find average fare by class → sort highest to lowest
# 2. Find survival rate by gender → sort highest to lowest
# 3. Find total passengers per embarkation port → sort highest to lowest
# 4. Find average age per class → sort youngest to oldest class

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

average_fare = df.groupby("Pclass")["Fare"].mean().round(2)
print(average_fare.sort_values(ascending=False))

survival_rate = (df.groupby("Sex")["Survived"].mean() * 100).round(2)
print(survival_rate.sort_values(ascending=False))

total_passengers = df.groupby(["Embarked"]).size()
print(total_passengers.sort_values(ascending=False))

average_age = df.groupby("Pclass")["Age"].mean().round(2)
print(average_age.sort_values())


# Using Titanic dataset:
# 1. Count passengers by gender using size()
# 2. Count Age values by gender using count()
# 3. Print both results and compare — why are they different?
# 4. Which column has the most missing values?
#    Use count() vs size() to find out
#    hint: size() - count() = missing values


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

total_passengers = df.groupby("Sex").size()
print(total_passengers)

age_count = df.groupby("Sex")["Age"].count()
print(age_count)

print("\nDifference (Missing Ages):")
print(total_passengers - age_count)


total = df.groupby("Sex").size()
print("Missing values per column:")
print("=" * 30)

max_missing = 0
max_column = ""

for col in df.columns:
    count = df.groupby("Sex")[col].count()
    missing = total - count
    total_missing = missing.sum()
    if total_missing > 0:
        print(f"{col}: {total_missing} missing")

        if total_missing > max_missing:
            max_missing = total_missing
            max_column = col

print("=" * 30)
print(f" Most missing: {max_column} ({max_missing} values)")


# Using Titanic dataset, answer these questions
# using groupby only — no manual filtering!
#
# Print this report:
#
# ═══════════════════════════════════════
#      SURVIVAL ANALYSIS BY GROUPS
# ═══════════════════════════════════════
#
# ── BY GENDER ───────────────────────────
# Gender    Total    Survived    Rate
# female    314      233         74.20%
# male      577      109         18.89%
#
# ── BY CLASS ────────────────────────────
# Class    Total    Survived    Rate
# 1        216      136         62.96%
# 2        184      87          47.28%
# 3        491      119         24.24%
#
# ── BY PORT ─────────────────────────────
# Port    Total    Survived    Rate
# C       168      93          55.36%
# Q       77       30          38.96%
# S       644      217         33.70%
#
# ── FARE ANALYSIS BY CLASS ───────────────
# Class    Mean      Max       Min
# 1        84.15     512.33    0.00
# 2        20.66     73.50     0.00
# 3        13.68     69.55     0.00
# ═══════════════════════════════════════

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

total = df.groupby("Sex").size()
survival = df.groupby("Sex")["Survived"].sum()
rate = (df.groupby("Sex")["Survived"].mean() * 100).round(2)

result = pd.DataFrame({
    "Total": total,
    "Survival": survival,
    "Rate": rate
})
print(result)


total = df.groupby("Pclass").size()
survival = df.groupby("Pclass")["Survived"].sum()
rate = (df.groupby("Pclass")["Survived"].mean() * 100).round(2)

result = pd.DataFrame({
    "Total": total,
    "Survival": survival,
    "Rate": rate
})
print(result)


total = df.groupby("Embarked").size()
survival = df.groupby("Embarked")["Survived"].sum()
rate = (df.groupby("Embarked")["Survived"].mean() * 100).round(2)

result = pd.DataFrame({
    "Total": total,
    "Survival": survival,
    "Rate": rate
})
print(result)

total = df.groupby("Pclass").size()
survival = df.groupby("Pclass")["Survived"].sum()
rate = (df.groupby("Pclass")["Survived"].mean() * 100).round(2)

result = pd.DataFrame({
    "Total": total,
    "Survival": survival,
    "Rate": rate
})
print(result)

fare_analysis = df.groupby("Pclass")["Fare"].agg(["mean", "max", "min"]).round(2)
print(fare_analysis)