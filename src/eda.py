
import pandas as pd

# Load cleaned sales data
df = pd.read_csv("data/processed/cleaned_sales.csv")

# Display the dataset
print(df)

#adding the new column-Revenue
df['Revenue']=df['Quantity']*df['Price']
print(df)

#calculating the total revenue
total_revenue=df['Revenue'].sum()
print(f"Total_Revenue:{total_revenue}")

# using groupby()
df.groupby('Product')

# Calculate revenue for each product
product_sales = df.groupby("Product")["Revenue"].sum()

print(product_sales)

#sorting the productsales
product_sales = product_sales.sort_values(ascending=False)

print(product_sales)

# Calculate revenue city-wise
city_sales = df.groupby("City")["Revenue"].sum()

# Sort from highest to lowest
city_sales = city_sales.sort_values(ascending=False)

print(city_sales)


# Total number of orders
total_orders = df["OrderID"].nunique()

# Total quantity sold
total_quantity = df["Quantity"].sum()

print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)


#creating a bar chart

import matplotlib.pyplot as plt


#

plt.figure(figsize=(10, 6))

product_sales.plot(kind="bar")

plt.title("Revenue by Product", fontsize=16)
plt.xlabel("Product")
plt.ylabel("Revenue (INR)")

plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
