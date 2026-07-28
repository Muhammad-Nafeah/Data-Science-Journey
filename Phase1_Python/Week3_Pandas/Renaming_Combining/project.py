#Monthly Sales Data
# Your manager says:
# "We have sales data for 3 months
#  combine them into one annual report"
#
# Create monthly data:

# january = pd.DataFrame({
#     "Product":  ["Laptop", "Phone", "Tablet"],
#     "Sales":    [50, 120, 30],
#     "Revenue":  [250000, 180000, 60000],
#     "Month":    ["January", "January", "January"]
# })

# february = pd.DataFrame({
#     "Product":  ["Laptop", "Phone", "Headphones"],
#     "Sales":    [45, 100, 80],
#     "Revenue":  [225000, 150000, 40000],
#     "Month":    ["February", "February", "February"]
# })

# march = pd.DataFrame({
#     "Product":  ["Laptop", "Tablet", "Headphones"],
#     "Sales":    [60, 40, 90],
#     "Revenue":  [300000, 80000, 45000],
#     "Month":    ["March", "March", "March"]
# })

# Task:
# 1. Stack all 3 months using concat()
#    with ignore_index=True
#    print full combined DataFrame
#
# 2. Total revenue for all 3 months combined
#
# 3. Which product had highest total sales?
#    hint: groupby Product → sum Sales → sort
#
# 4. Which month had highest total revenue?
#    hint: groupby Month → sum Revenue
#
# 5. Rename columns:
#    "Sales"   → "Units_Sold"
#    "Revenue" → "Total_Revenue_PKR"
#    print updated DataFrame

import pandas as pd

january = pd.DataFrame({
    "Product":  ["Laptop", "Phone", "Tablet"],
    "Sales":    [50, 120, 30],
    "Revenue":  [250000, 180000, 60000],
    "Month":    ["January", "January", "January"]
})

february = pd.DataFrame({
    "Product":  ["Laptop", "Phone", "Headphones"],
    "Sales":    [45, 100, 80],
    "Revenue":  [225000, 150000, 40000],
    "Month":    ["February", "February", "February"]
})

march = pd.DataFrame({
    "Product":  ["Laptop", "Tablet", "Headphones"],
    "Sales":    [60, 40, 90],
    "Revenue":  [300000, 80000, 45000],
    "Month":    ["March", "March", "March"]
})

combined_month = pd.concat([january,february,march],ignore_index=True)
print(combined_month)

print(f"Total Revenue: {combined_month['Revenue'].sum()} PKR")

highest_sales_by_product = (combined_month.groupby("Product")["Sales"].sum().sort_values(ascending=False))
print(highest_sales_by_product)

highest_revenue_by_month = (combined_month.groupby("Month")["Revenue"].sum().sort_values(ascending=False))
print(highest_revenue_by_month)

combined_month.rename(columns={
    "Sales": "Units_Sold",
    "Revenue": "Total_Revenue_PKR"
},inplace=True)

print("Updated DataFrame")
print(combined_month)



#Cricket IPL Dataset
# Download IPL dataset from Kaggle
# It usually has 2 files:
# matches.csv  — match details
# deliveries.csv — ball by ball data
#
# Task:
# 1. Load both files
# 2. Print shape of both
# 3. Print columns of both
# 4. Merge both on "id" column (matches) and "match_id" (deliveries)
#    hint: pd.merge(matches, deliveries,
#                   left_on="id", right_on="match_id")
# 5. After merging:
#    Which team won the most matches?
#    Which batsman scored the most runs?
#    Which season had the most matches?

import pandas as pd

matches_df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/matches.csv")
deliveries_df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/deliveries.csv")

print(f"{matches_df.shape} ---- {deliveries_df.shape}")

print(matches_df.columns.to_list())
print(deliveries_df.columns.to_list())

print(f"{matches_df["id"]}")
print(f"{deliveries_df["match_id"]}")

merge_id = pd.merge(matches_df,deliveries_df,left_on="id",right_on="match_id")
print(merge_id)

print(matches_df["winner"].value_counts().idxmax())

print(deliveries_df["batsman"].value_counts)

runs_by_batsman = deliveries_df.groupby("batsman")["batsman_runs"].sum()

print("Top Scorer:", runs_by_batsman.idxmax())
print("Runs:", runs_by_batsman.max())

print(f"Most Matches Played in the season: {matches_df.groupby("season").size().idxmax()}")

# Netflix Dataset Challenge
# Download Netflix Movies and TV Shows dataset from Kaggle
# File: netflix_titles.csv
#
# Task:
# 1. Load and inspect the dataset
# 2. Split into two DataFrames:
#    movies  = df[df["type"] == "Movie"]
#    tvshows = df[df["type"] == "TV Show"]
#
# 3. Rename columns:
#    "listed_in" → "Genre"
#    "release_year" → "Release_Year"
#    "date_added" → "Date_Added_Netflix"
#
# 4. Stack movies and tvshows back using concat()
#    confirm total rows match original
#
# 5. Create a summary DataFrame:
#    Total Movies, Total TV Shows, Total Content
#    using concat() to combine the counts

import pandas as pd

df = pd.read_csv("Phase1_Python/Week3_Pandas/datasets/netflix_titles.csv")

print(df.shape)

print(df.columns.to_list())

movies = df[df["type"] == "Movie"]
tvshows = df[df["type"] == "TV Show"]

df.rename(columns={
    "listed_in": "Genre",
    "release_year": "Release_Year",
    "date_added": "Date_Added_Netflix"
},inplace=True)
print(df.columns.to_list())

combined_result = pd.concat([movies,tvshows],ignore_index=True)
print(len(combined_result))

movies_count = pd.DataFrame({
    "Category": ["Total Movies"],
    "Count": [len(movies)]
})
tvshows_count = pd.DataFrame({
    "Category": ["Total TV Shows"],
    "Count": [len(tvshows)]
})
total_content = pd.DataFrame({
    "Category": ["Total Content"],
    "Count": [len(df)]
})

summary = pd.concat([movies_count,tvshows_count,total_content],ignore_index=True)
print(summary)

