import sqlite3

conn = sqlite3.connect("sales.db")

customers.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

-- 15 SQL Queries

SELECT * FROM customers;

SELECT * FROM products;

SELECT * FROM orders;

SELECT * FROM customers
WHERE region='North';

SELECT * FROM products
ORDER BY price DESC;

SELECT category,
SUM(price)
FROM products
GROUP BY category;

SELECT region,
COUNT(*)
FROM customers
GROUP BY region;

SELECT AVG(price)
FROM products;

SELECT MAX(price)
FROM products;

SELECT MIN(price)
FROM products;

SELECT c.name,p.product_name
FROM orders o
JOIN customers c
ON o.customer_id=c.customer_id
JOIN products p
ON o.product_id=p.product_id;

SELECT category,
COUNT(*)
FROM products
GROUP BY category;

SELECT *
FROM products
WHERE price >
(
SELECT AVG(price)
FROM products
);

SELECT region,
SUM(quantity)
FROM orders o
JOIN customers c
ON o.customer_id=c.customer_id
GROUP BY region;

SELECT product_name
FROM products
WHERE price=
(
SELECT MAX(price)
FROM products
);