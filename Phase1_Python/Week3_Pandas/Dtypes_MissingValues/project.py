# Your manager says:
# "Apply the complete data cleaning workflow
#  on the Titanic dataset — follow these steps exactly"
#
# Step 1 → INSPECT
#   Print df.info()
#   Print df.isnull().sum()
#   Print df.dtypes
#
# Step 2 → CLEAN MISSING VALUES
#   Age      → fillna with median
#   Embarked → fillna with mode
#   Cabin    → fillna with "Unknown"
#
# Step 3 → STANDARDIZE VALUES
#   Sex column → replace male/female with M/F
#
# Step 4 → CONVERT DATA TYPES
#   PassengerId → convert to string
#   Pclass      → convert to string
#
# Step 5 → VERIFY
#   Print df.isnull().sum() → should be all zeros
#   Print df.dtypes → confirm type changes
#   Print df.head(10) → final clean dataset
#
# Step 6 → SAVE
#   Save cleaned dataset to:
#   "datasets/Titanic_Cleaned.csv"
#   with index=False
#
# Print completion message:
# "✅ Data cleaning complete! Saved to Titanic_Cleaned.csv"

import pandas as pd

#Load data
df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

df.info()
print(df.isnull().sum())
print(df.dtypes)

df["Age"] = df["Age"].fillna(df["Age"].median()).round(2)
print(df["Age"])

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df["Embarked"])

df["Cabin"] = df["Cabin"].fillna("unknown")
print(df["Cabin"])

df["Sex"] = df["Sex"].replace({
    "male":"M",
    "female":"F"
})
print(df["Sex"])

df["PassengerId"] = df["PassengerId"].astype(str)
df["Pclass"] = df["Pclass"].astype(str)
df["Fare"] = df["Fare"].astype(int)

print(df.isnull().sum())
print(df.dtypes)
print(df.head(10))

save_data = df.to_csv("Phase1_Python/Week3_Pandas/datasets/Titanic_Cleaned.csv",index=False)

print("\nData cleaning complete! Saved to Titanic_Cleaned.csv")




