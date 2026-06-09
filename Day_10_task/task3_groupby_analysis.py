merged = (
    orders.merge(customers, on="customer_id")
          .merge(products, on="product_id")
)

merged["revenue"] = (
    merged["quantity"] * merged["price"]
)

print("\nSales by Region")
print(
    merged.groupby("region")["revenue"].sum()
)

print("\nSales by Category")
print(
    merged.groupby("category")["revenue"].sum()
)

print("\nMulti-level GroupBy")
print(
    merged.groupby(
        ["region", "segment"]
    )["revenue"].sum()
)