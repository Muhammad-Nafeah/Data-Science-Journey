# Your manager says:
# "The Titanic column names are not client friendly
#  rename them before sending the report"
#
# Using Titanic dataset:
# 1. Rename these columns:
#    "PassengerId" → "Passenger_ID"
#    "Pclass"      → "Ticket_Class"
#    "SibSp"       → "Siblings_Spouses"
#    "Parch"       → "Parents_Children"
#    "Embarked"    → "Boarding_Port"
#
# 2. Print column names before and after
#
# 3. Rename the index axis title to "Record_Number"
#    using rename_axis()
#
# 4. Set "Passenger_ID" as the index
#    using set_index()
#
# 5. Print first 5 rows after all changes

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

print("Before:")
print(df.columns.tolist())

df = df.rename(columns={
    "PassengerId": "Passenger_ID",
    "Pclass": "Ticket_Class",
    "SibSp": "Siblings_Spouses",
    "Parch": "Parents_Children",
    "Embarked": "Boarding_Port"
})
print("After:")
print(df.columns.tolist())

df = df.rename_axis("Record_Number")

df = df.set_index("Passenger_ID")

print(df.head())


# Your manager says:
# "We have Titanic data split into 3 groups
#  stack them back into one DataFrame"
#
# Split Titanic into 3 groups:
# first_class  = df[df["Pclass"] == 1]
# second_class = df[df["Pclass"] == 2]
# third_class  = df[df["Pclass"] == 3]
#
# Task:
# 1. Stack all 3 using concat()
#    print total rows — should be 891
#
# 2. Stack with ignore_index=True
#    print index — should be 0 to 890
#
# 3. Stack WITHOUT ignore_index
#    print index — what do you notice?
#    why is it different?
#
# 4. Stack horizontally using axis=1
#    print shape — what happens?
#    why does shape change?
#
# 5. Split Titanic by gender and stack back:
#    male_df   = df[df["Sex"] == "male"]
#    female_df = df[df["Sex"] == "female"]
#    stack both → confirm total rows = 891


import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

first_class = df[df["Pclass"] == 1]
second_class = df[df["Pclass"] == 2]
third_class = df[df["Pclass"] == 3]

combined_df = pd.concat([first_class,second_class,third_class])
print(len(combined_df))


first_class = df[df["Pclass"] == 1]
second_class = df[df["Pclass"] == 2]
third_class = df[df["Pclass"] == 3]

combined_df = pd.concat([first_class,second_class,third_class],ignore_index=True)
print(combined_df.index)


combined_df = pd.concat([first_class,second_class,third_class])
print(combined_df.index)

combined_df = pd.concat([first_class,second_class,third_class],axis=1)
print(combined_df.shape)

male_df = df[df["Sex"] == "male"]
female_df = df[df["Sex"] == "female"]

combined_df = pd.concat([male_df,female_df],ignore_index=True)
print(len(combined_df))



# Your manager says:
# "We have passenger info in one table
#  and ticket prices in another
#  merge them together"
#
# Create these two DataFrames:

# passengers = pd.DataFrame({
#     "PassengerID": [1, 2, 3, 4, 5],
#     "Name": ["Ahmed", "Sara", "Ali", "Zara", "Usman"],
#     "Age":  [22, 35, 28, 19, 45],
#     "City": ["Karachi", "Lahore", "Islamabad", "Karachi", "Peshawar"]
# })

# tickets = pd.DataFrame({
#     "PassengerID": [1, 2, 3, 4, 6],
#     "Ticket_Class": ["First", "Second", "Third", "First", "Second"],
#     "Fare": [500, 200, 100, 450, 180]
# })

# Notice PassengerID 5 (Usman) has no ticket
# Notice PassengerID 6 has a ticket but no passenger info
#
# Task:
# 1. Inner merge — only matching passengers
#    who gets dropped and why?
#
# 2. Left merge — keep all passengers
#    what happens to Usman? → NaN in ticket columns
#
# 3. Right merge — keep all tickets
#    what happens to ticket 6? → NaN in passenger columns
#
# 4. Outer merge — keep everything
#    print shape and explain the result
#
# 5. For each merge type print:
#    "Inner merge: X rows — only matched passengers"
#    "Left merge:  X rows — all passengers kept"
#    "Right merge: X rows — all tickets kept"
#    "Outer merge: X rows — everything kept"

import pandas as pd

passengers = pd.DataFrame({
    "PassengerID": [1, 2, 3, 4, 5],
    "Name": ["Ahmed", "Sara", "Ali", "Zara", "Usman"],
    "Age":  [22, 35, 28, 19, 45],
    "City": ["Karachi", "Lahore", "Islamabad", "Karachi", "Peshawar"]
})

tickets = pd.DataFrame({
    "PassengerID": [1, 2, 3, 4, 6],
    "Ticket_Class": ["First", "Second", "Third", "First", "Second"],
    "Fare": [500, 200, 100, 450, 180]
})

inner_merge = pd.merge(passengers,tickets,on="PassengerID",how="inner")

left_merge = pd.merge(passengers,tickets,on="PassengerID",how="left")

right_merge = pd.merge(passengers,tickets,on="PassengerID",how="right")

outer_merge = pd.merge(passengers,tickets,on="PassengerID",how="outer")

print(f"Inner merge: {len(inner_merge)} rows - only matched passengers")
print(inner_merge)
print(f"Left merge: {len(left_merge)} rows - all passengers kept")
print(left_merge)
print(f"Right merge: {len(right_merge)} rows - all tickets kept")
print(right_merge)
print(f"Outer merge: {len(outer_merge)} rows - everything kept")
print(outer_merge)



# Your manager says:
# "Join passenger details with their survival info
#  using the index"
#
# Create two DataFrames from Titanic:

# passenger_info = df[["Name", "Age", "Sex"]].set_index("Name")
# survival_info  = df[["Name", "Survived", "Pclass"]].set_index("Name")

# Task:
# 1. Join both DataFrames using join()
#    print first 10 rows
#
# 2. What happens if both DataFrames have
#    a column with the same name?
#    Create this situation and use lsuffix and rsuffix:

# df1 = df[["Name", "Age", "Fare"]].set_index("Name")
# df2 = df[["Name", "Fare", "Survived"]].set_index("Name")

#    Both have "Fare" column!
#    Join using lsuffix="_original" rsuffix="_copy"
#    print result

import pandas as pd
df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/Titanic-Dataset.csv")

passenger_info = df[["Name","Age","Sex"]].set_index("Name")
survival_info = df[["Name","Survived","Pclass"]].set_index("Name")

combined_df = passenger_info.join(survival_info)
print(combined_df.head(10))

df1 = df[["Name", "Age", "Fare"]].set_index("Name")
df2 = df[["Name", "Fare", "Survived"]].set_index("Name")

result = df1.join(df2,lsuffix="_original",rsuffix="_copy")
print(result)


