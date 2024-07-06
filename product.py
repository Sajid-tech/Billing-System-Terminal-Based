# billing_system/product.py
import sqlite3
from tabulate import tabulate

# View products function
def view_products(user_id):
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    c.execute("SELECT id, name, price, description, category, quantity FROM products")
    products = c.fetchall()
    if products:
        print("\n--- Products ---")
        print(tabulate(products, headers=["ID", "Name", "Price", "Description", "Category", "Quantity"]))
    else:
        print("No products found.")
    conn.close()



# Add product function
def add_product():
    print("\n--- Add Product ---")
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    description = input("Enter product description: ")
    category = input("Enter product category: ")
    quantity = int(input("Enter product quantity: "))
    
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO products (name, price, description, category, quantity) VALUES (?, ?, ?, ?, ?)", 
                  (name, price, description, category, quantity))
        conn.commit()
        print("Product added successfully!")
    except sqlite3.IntegrityError:
        print("Product already exists.")
    conn.close()



# Update product function
def update_product():
    print("\n--- Update Product ---")
    product_id = int(input("Enter product ID to update: "))
    new_name = input("Enter new product name: ")
    new_price = float(input("Enter new product price: "))
    new_description = input("Enter new product description: ")
    new_category = input("Enter new product category: ")
    new_quantity = int(input("Enter new product quantity: "))
    
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    try:
        c.execute("UPDATE products SET name = ?, price = ?, description = ?, category = ?, quantity = ? WHERE id = ?", 
                  (new_name, new_price, new_description, new_category, new_quantity, product_id))
        conn.commit()
        print("Product updated successfully!")
    except sqlite3.Error:
        print("Failed to update product.")
    conn.close()

# Delete product function
def delete_product():
    print("\n--- Delete Product ---")
    product_id = int(input("Enter product ID to delete: "))
    
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    try:
        c.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        print("Product deleted successfully!")
    except sqlite3.Error:
        print("Failed to delete product.")
    conn.close()
