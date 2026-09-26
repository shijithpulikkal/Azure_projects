import pandas as pd

orders = pd.read_csv(
    "olist_orders_dataset.csv",
    parse_dates=["order_purchase_timestamp"]
)

order_items = pd.read_csv(
    "olist_order_items_dataset.csv"
)

df = order_items.merge(
    orders[["order_id", "order_purchase_timestamp"]],
    on="order_id"
)

df["date"] = df["order_purchase_timestamp"].dt.date

daily = df.groupby("date").agg(
    daily_revenue=("price", "sum"),
    daily_order_count=("order_id", "nunique")
).reset_index()

daily["date"] = pd.to_datetime(daily["date"])
daily = daily.sort_values("date")

full_range = pd.date_range(
    daily["date"].min(),
    daily["date"].max(),
    freq="D"
)

daily = (
    daily.set_index("date")
         .reindex(full_range)
         .fillna(0)
         .rename_axis("date")
         .reset_index()
)

daily.to_csv("forecast_input.csv", index=False)

print(daily.head())
print(daily.tail())