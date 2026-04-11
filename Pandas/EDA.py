#Importing Libraries
import pandas as pd 
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns

#Loading csvs 
customers = pd.read_csv("Ecommerce Sales/olist_customers_dataset.csv")
geolocation=pd.read_csv("Ecommerce Sales/olist_geolocation_dataset.csv")
order_items=pd.read_csv("Ecommerce Sales/olist_order_items_dataset.csv")
order_payments=pd.read_csv("Ecommerce Sales/olist_order_payments_dataset.csv")
orders =pd.read_csv("Ecommerce Sales/olist_orders_dataset.csv")
products =pd.read_csv("Ecommerce Sales/olist_products_dataset.csv")

#Merging tables
df = orders.merge(customers,on="customer_id",how="left")\
      .merge(order_items,on="order_id",how="left")\
      .merge(products,on="product_id",how="left")\
      .merge(order_payments,on="order_id",how="left")

df["total"] =df["freight_value"] + df["price"]

#KPIS
total_revenue = df["total"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
aov = df.groupby("order_id")["total"].sum().mean()
print("AOV:", aov)
print("Total Revenue:", round(total_revenue,2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)

#Top 10 Products
top_products = (
    df.groupby("product_id")["total"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)
print(top_products)

#Revenue by Category
revenue_by_category = (
    df.groupby("product_category_name")["total"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
print(revenue_by_category)

#Visualization
revenue_by_category.head(10).plot(
    x="product_category_name",
    y="total",
    kind="bar",
    title="Top 10 Categories by Revenue"
)
plt.xticks(rotation=45)
plt.show()

#IMPACT OF DELIVERY DELAYS
df["delay_days"] = (
    df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
).dt.days

df["is_delayed"] = df["delay_days"] > 0

delay_impact = df.groupby("is_delayed")["order_id"].count()
print(delay_impact)
