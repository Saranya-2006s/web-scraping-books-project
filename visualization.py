import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv("books_data.csv")

# ----------------------------
# Clean Price Column
# ----------------------------
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True)
df["Price"] = pd.to_numeric(df["Price"])

# ----------------------------
# Convert Rating to Numeric
# ----------------------------
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["Rating"] = df["Rating"].map(rating_map)

# ----------------------------
# Create 2x2 Dashboard Layout
# ----------------------------
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# ----------------------------
# 1. Price Distribution
# ----------------------------
axes[0, 0].hist(df["Price"], bins=10)
axes[0, 0].set_title("Price Distribution")
axes[0, 0].set_xlabel("Price (£)")
axes[0, 0].set_ylabel("Number of Books")

# ----------------------------
# 2. Rating Distribution
# ----------------------------
df["Rating"].value_counts().sort_index().plot(
    kind="bar", ax=axes[0, 1]
)
axes[0, 1].set_title("Rating Distribution")
axes[0, 1].set_xlabel("Rating")
axes[0, 1].set_ylabel("Number of Books")

# ----------------------------
# 3. Average Price by Rating
# ----------------------------
df.groupby("Rating")["Price"].mean().plot(
    kind="bar", ax=axes[1, 0]
)
axes[1, 0].set_title("Average Price by Rating")
axes[1, 0].set_xlabel("Rating")
axes[1, 0].set_ylabel("Average Price (£)")

# ----------------------------
# 4. Top 10 Most Expensive Books
# ----------------------------
top_books = df.sort_values("Price", ascending=False).head(10)

short_titles = top_books["Title"].str.slice(0, 30) + "..."
axes[1, 1].barh(short_titles, top_books["Price"])

axes[1, 1].set_title("Top 10 Expensive Books")
axes[1, 1].set_xlabel("Price (£)")
axes[1, 1].invert_yaxis()

# ----------------------------
# Adjust Layout & Show
# ----------------------------
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
