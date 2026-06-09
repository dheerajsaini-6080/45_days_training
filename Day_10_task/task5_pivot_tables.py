merged["month"] = (
    merged["order_date"]
    .dt.month_name()
)

pivot1 = pd.pivot_table(
    merged,
    values="revenue",
    index="region",
    columns="month",
    aggfunc="sum"
)

pivot2 = pd.pivot_table(
    merged,
    values="revenue",
    index="category",
    columns="segment",
    aggfunc="sum"
)

print(pivot1)
print()
print(pivot2)