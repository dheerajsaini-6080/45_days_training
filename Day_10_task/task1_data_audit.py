import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

tables = {
    "Customers": customers,
    "Products": products,
    "Orders": orders
}

for name, df in tables.items():
    print(f"\n{name}")
    print("=" * 40)
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)
    print("\nNull Values:")
    print(df.isnull().sum())
    print("\nDuplicates:", df.duplicated().sum())
    print("\nUnique Counts:")
    print(df.nunique())