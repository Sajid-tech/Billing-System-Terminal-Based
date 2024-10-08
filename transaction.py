# billing_system/transaction.py
import sqlite3
from datetime import datetime
import mysql.connector as mysql
from tabulate import tabulate

# View transactions function
def view_transactions(user_id):
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    c.execute('''SELECT transactions.id, products.name, transactions.quantity, transactions.date, 
                 products.price * transactions.quantity AS total_price
                 FROM transactions 
                 JOIN products ON transactions.product_id = products.id
                 WHERE transactions.user_id = %s''', (user_id,))
    transactions = c.fetchall()
    if transactions:
        print("\n--- Transactions ---")
        print(tabulate(transactions, headers=["Transaction ID", "Product Name", "Quantity", "Date", "Total Price"]))
    else:
        print("No transactions found.")
    conn.close()
# Generate bill function
def generate_bill(user_id):
    print("\n--- Generate Bill ---")
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))
    
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    try:
        c.execute("SELECT name, price, quantity FROM products WHERE id = %s", (product_id,))
        product = c.fetchone()
        if product:
            product_name, product_price, product_quantity = product
            if product_quantity < quantity:
                print(f"Insufficient stock for {product_name}. Available quantity: {product_quantity}")
            else:
                date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                total_price = product_price * quantity
                c.execute("INSERT INTO transactions (user_id, product_id, quantity, date) VALUES (%s, %s, %s, %s)",
                          (user_id, product_id, quantity, date))
                c.execute("UPDATE products SET quantity = quantity - %s WHERE id = %s", (quantity, product_id))
                conn.commit()
                print(f"Bill generated successfully!\nProduct: {product_name}\nQuantity: {quantity}\nTotal Price: {total_price}\nDate: {date}")
        else:
            print("Product not found.")
    except mysql.Error as e:
        print(f"Error: {e}")
    finally:
        conn.close()

# View all transactions function for admin
def view_all_transactions():
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    c.execute('''SELECT transactions.id, users.username, products.name, transactions.quantity, transactions.date, 
                 products.price * transactions.quantity AS total_price
                 FROM transactions 
                 JOIN users ON transactions.user_id = users.id
                 JOIN products ON transactions.product_id = products.id''')
    transactions = c.fetchall()
    if transactions:
        print("\n--- All Transactions ---")
        print(tabulate(transactions, headers=["Transaction ID", "Username", "Product Name", "Quantity", "Date", "Total Price"]))
    else:
        print("No transactions found.")
    conn.close()
