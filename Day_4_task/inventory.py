# Mini Inventory System
# Combines OOP and CSV file handling.

import csv


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_value(self) -> float:
        return sum(
            p.price * p.quantity
            for p in self.products
        )

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product

        return None

    def save_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["name", "price", "quantity"]
            )

            for product in self.products:
                writer.writerow(
                    [
                        product.name,
                        product.price,
                        product.quantity
                    ]
                )

    def load_from_csv(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            self.products = []

            for row in reader:
                self.products.append(
                    Product(
                        row["name"],
                        float(row["price"]),
                        int(row["quantity"])
                    )
                )


inventory = Inventory()

inventory.add_product(
    Product("Laptop", 50000, 2)
)

inventory.add_product(
    Product("Mouse", 500, 10)
)

print("Total Value:")
print(inventory.total_value())

inventory.save_to_csv(
    "inventory.csv"
)

inventory.load_from_csv(
    "inventory.csv"
)

product = inventory.find_product(
    "Laptop"
)

if product:
    print(product.name, product.price)

