# -------------------------------
# 📌 Task 5: Data Analysis on CSV
# -------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load CSV file
# Make sure your CSV file name is "sales.csv"
df = pd.read_csv("sales.csv")

print("First 5 rows of data:")
print(df.head())


# 2️⃣ Add Total Sales column
df["Total"] = df["Units"] * df["Price"]

print("\nData after adding Total column:")
print(df.head())


# 3️⃣ Total Sales by Product
sales_by_product = df.groupby("Product")["Total"].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)

# 📊 Bar chart for sales by product
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()


# 4️⃣ Daily Sales
daily_sales = df.groupby("Date")["Total"].sum()
print("\nDaily Sales:")
print(daily_sales)

# 📊 Line chart for daily sales
daily_sales.plot(kind="line")
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# 5️⃣ Units Sold by Product
units_by_product = df.groupby("Product")["Units"].sum()
print("\nUnits Sold by Product:")
print(units_by_product)

# 📊 Pie chart
units_by_product.plot(kind="pie", autopct="%1.1f%%")
plt.title("Units Sold Percentage by Product")
plt.ylabel("")
plt.show()


# 6️⃣ Summary Statistics
print("\nSummary Statistics:")
print(df.describe())
