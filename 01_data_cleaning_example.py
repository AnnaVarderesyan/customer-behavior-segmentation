"""Ուսուցողական օրինակ. Fabric notebook-ի բնօրինակը չէ։"""
import pandas as pd

# Փոխարինեք այս անունները իրական Lakehouse CSV ուղիներով։
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
items = pd.read_csv("order_items.csv")
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
data = orders.merge(customers, on="customer_id").merge(items, on="order_id")
data = data.loc[(data["order_status"] == "delivered") & (data["price"] > 0) & data["customer_unique_id"].notna()].copy()
print("Valid item rows:", len(data))
