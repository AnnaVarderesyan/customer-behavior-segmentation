"""Ուսուցողական օրինակ. Օգտագործում է 01-ի data փոփոխականը։"""
import pandas as pd

def calculate_rfm(data):
    reference_date = data["order_purchase_timestamp"].max() + pd.Timedelta(days=1)
    rfm = data.groupby("customer_unique_id").agg(
        LastPurchase=("order_purchase_timestamp", "max"),
        Frequency=("order_id", "nunique"),
        Monetary=("price", "sum"),
    )
    rfm["Recency"] = (reference_date - rfm["LastPurchase"]).dt.days
    return rfm.drop(columns="LastPurchase").reset_index()

# Monetary = price.sum(), քանի որ order_items-ում quantity դաշտ չկա։
