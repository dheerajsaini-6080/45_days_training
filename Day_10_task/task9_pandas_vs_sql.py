pandas_result = (
    merged.groupby("region")
    ["revenue"]
    .sum()
)

print("Pandas Result")
print(pandas_result)


# SQL
SELECT region,
SUM(quantity * price) AS revenue
FROM orders o
JOIN customers c
ON o.customer_id=c.customer_id
JOIN products p
ON o.product_id=p.product_id
GROUP BY region;


# Comparison
Pandas is more flexible for data analysis and visualization.

SQL is more readable for database querying and reporting.

Both produce the same business result when calculating regional revenue.