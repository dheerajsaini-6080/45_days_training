customers.columns = customers.columns.str.lower()
products.columns = products.columns.str.lower()
orders.columns = orders.columns.str.lower()

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

customers.fillna("Unknown", inplace=True)
products.fillna(0, inplace=True)

print("Data cleaned successfully")