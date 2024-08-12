# billing_system/product.py
import sqlite3
import mysql.connector as mysql
from tabulate import tabulate

# View products function
def view_products(user_id):
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
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
    
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    try:
        c.execute("INSERT INTO products (name, price, description, category, quantity) VALUES (%s, %s, %s, %s, %s)", 
                  (name, price, description, category, quantity))
        conn.commit()
        print("Product added successfully!")
    except mysql.Error as e:
        print(f"Error: {e}")
    finally:
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
    
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    try:
        c.execute("UPDATE products SET name = %s, price = %s, description = %s, category = %s, quantity = %s WHERE id = %s", 
                  (new_name, new_price, new_description, new_category, new_quantity, product_id))
        conn.commit()
        print("Product updated successfully!")
    except mysql.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# Delete product function
def delete_product():
    print("\n--- Delete Product ---")
    product_id = int(input("Enter product ID to delete: "))
    
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    try:
        c.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()
        print("Product deleted successfully!")
    except mysql.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()
