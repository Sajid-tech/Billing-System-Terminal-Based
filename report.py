# billing_system/report.py
import sqlite3
from tabulate import tabulate


# Generate sales report function for admin
def generate_sales_report():
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    c.execute('''SELECT products.name, SUM(transactions.quantity) AS total_quantity_sold, 
                 SUM(products.price * transactions.quantity) AS total_sales
                 FROM transactions 
                 JOIN products ON transactions.product_id = products.id
                 GROUP BY products.name''')
    sales_report = c.fetchall()
    if sales_report:
        print("\n--- Sales Report ---")
        print(tabulate(sales_report, headers=["Product Name", "Total Quantity Sold", "Total Sales"]))
    else:
        print("No sales data available.")
    conn.close()


# Generate user activity report function for admin
def generate_user_activity_report():
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    c.execute('''SELECT users.username, COUNT(transactions.id) AS total_transactions, 
                 SUM(products.price * transactions.quantity) AS total_spent
                 FROM transactions 
                 JOIN users ON transactions.user_id = users.id
                 JOIN products ON transactions.product_id = products.id
                 GROUP BY users.username''')
    user_activity_report = c.fetchall()
    if user_activity_report:
        print("\n--- User Activity Report ---")
        print(tabulate(user_activity_report, headers=["Username", "Total Transactions", "Total Spent"]))
    else:
        print("No user activity data available.")
    conn.close()
