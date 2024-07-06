# billing_system/inventory.py
import sqlite3
from tabulate import tabulate

# Inventory notification function for admin
def inventory_notification():
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    c.execute("SELECT name, quantity FROM products WHERE quantity <= 5")
    low_stock_products = c.fetchall()
    if low_stock_products:
        print("\n--- Low Stock Products ---")
        for product in low_stock_products:
            print(f"Product: {product[0]}, Quantity: {product[1]}")
    else:
        print("No low stock products.")
    conn.close()


# Generate inventory report function for admin
def generate_inventory_report():
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    c.execute('''SELECT name, price, description, category, quantity 
                 FROM products''')
    inventory_report = c.fetchall()
    if inventory_report:
        print("\n--- Inventory Report ---")
        print(tabulate(inventory_report, headers=["Product Name", "Price", "Description", "Category", "Quantity"]))
    else:
        print("No inventory data available.")
    conn.close()

