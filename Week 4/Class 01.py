# Week 4 | Class 01: Pandas Series/DataFrames, CSV, selection and cleaning
# References:
# https://www.w3schools.com/python/pandas_tutorial.asp
# https://www.w3schools.com/python/pandas_csv.asp
# https://www.w3schools.com/python/pandas_cleaning.asp

import pandas as pd

data = {
    "student": ["Ali", "Sara", "Hamza", "Mina", "Noor"],
    "hours": [2, 4, None, 3, 5],
    "score": [55, 88, 72, None, 95],
    "city": ["Lahore", "Karachi", "Lahore", "Islamabad", "Karachi"],
}
df = pd.DataFrame(data)
print("Original:\n", df)
print("\nHead:\n", df.head())
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nMissing values:\n", df.isna().sum())

df["hours"] = df["hours"].fillna(df["hours"].median())
df["score"] = df["score"].fillna(df["score"].mean())
df["passed"] = df["score"] >= 50

print("\nCleaned:\n", df)
print("\nUnique cities:", df["city"].unique())
print("\nCity counts:\n", df["city"].value_counts())
print("\nScores above 75:\n", df.loc[df["score"] > 75, ["student", "score"]])

df.to_csv("week4_students_clean.csv", index=False)
print("\nSaved week4_students_clean.csv")
