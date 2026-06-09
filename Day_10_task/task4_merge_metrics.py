total_revenue = merged["revenue"].sum()

avg_order_value = (
    merged.groupby("order_id")["revenue"]
          .sum()
          .mean()
)

top_products = (
    merged.groupby("product_name")
          ["quantity"]
          .sum()
          .sort_values(ascending=False)
)

print("Total Revenue:", total_revenue)
print("Average Order Value:", avg_order_value)

print("\nTop Products")
print(top_products)