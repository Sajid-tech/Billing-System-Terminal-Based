# billing_system/search_filter.py
import sqlite3
import mysql.connector as mysql
from tabulate import tabulate

# Search and filter products function for admin
def search_filter_products():
    print("\n--- Search and Filter Products ---")
    search_term = input("Enter search term (leave blank for no search): ")
    min_price = input("Enter minimum price (leave blank for no filter): ")
    max_price = input("Enter maximum price (leave blank for no filter): ")
    
    query = "SELECT id, name, price, description, category, quantity FROM products WHERE 1=1"
    params = []
    
    if search_term:
        query += " AND (name LIKE %s OR description LIKE %s OR category LIKE %s)"
        params.extend([f"%{search_term}%", f"%{search_term}%", f"%{search_term}%"])
    
    if min_price:
        query += " AND price >= %s"
        params.append(float(min_price))
    
    if max_price:
        query += " AND price <= %s"
        params.append(float(max_price))
    
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    c.execute(query, params)
    products = c.fetchall()
    if products:
        print("\n--- Search and Filtered Products ---")
        print(tabulate(products, headers=["ID", "Name", "Price", "Description", "Category", "Quantity"]))
    else:
        print("No products found matching the criteria.")
    conn.close()



# Other search and filter functions can be added as needed
# Search and filter transactions function for admin
def search_filter_transactions():
    print("\n--- Search and Filter Transactions ---")
    username = input("Enter username (leave blank for no filter): ")
    product_name = input("Enter product name (leave blank for no filter): ")
    start_date = input("Enter start date (YYYY-MM-DD, leave blank for no filter): ")
    end_date = input("Enter end date (YYYY-MM-DD, leave blank for no filter): ")
    
    query = '''SELECT transactions.id, users.username, products.name, transactions.quantity, transactions.date, 
               products.price * transactions.quantity AS total_price
               FROM transactions 
               JOIN users ON transactions.user_id = users.id
               JOIN products ON transactions.product_id = products.id
               WHERE 1=1'''
    params = []
    
    if username:
        query += " AND users.username LIKE %s"
        params.append(f"%{username}%")
    
    if product_name:
        query += " AND products.name LIKE %s"
        params.append(f"%{product_name}%")
    
    if start_date:
        query += " AND date(transactions.date) >= %s"
        params.append(start_date)
    
    if end_date:
        query += " AND date(transactions.date) <= %s"
        params.append(end_date)
    
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    c.execute(query, params)
    transactions = c.fetchall()
    if transactions:
        print("\n--- Search and Filtered Transactions ---")
        print(tabulate(transactions, headers=["Transaction ID", "Username", "Product Name", "Quantity", "Date", "Total Price"]))
    else:
        print("No transactions found matching the criteria.")
    conn.close()
