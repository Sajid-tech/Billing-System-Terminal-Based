# billing_system/user.py

import mysql.connector as mysql
from tabulate import tabulate
from product import view_products, add_product , update_product, delete_product
from report import generate_sales_report, generate_user_activity_report
from inventory import inventory_notification, generate_inventory_report
from search_filter import search_filter_products, search_filter_transactions
from transaction import generate_bill,view_transactions, view_all_transactions


# View profile function
def view_profile(user_id):
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    c.execute("SELECT username, name, address, age FROM users WHERE id = %s", (user_id,))
    user = c.fetchone()
    if user:
        print(f"\n--- Profile ---\nUsername: {user[0]}\nName: {user[1]}\nAddress: {user[2]}\nAge: {user[3]}")
    else:
        print("User not found.")
    conn.close()


def view_users():
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    c.execute("SELECT id, username, name, address, age FROM users")
    users = c.fetchall()
    if users:
        print("\n--- Users ---")
        print(tabulate(users, headers=["User ID", "Username", "Name", "Address", "Age"]))
    else:
        print("No users found.")
    conn.close()




# User menu function with role-based access control
def user_menu(user_id, user_role):
    while True:
        print("\n--- User Menu ---")
        print("1--View Profile\n2--View Products\n3--Generate Bill\n4--View Transactions\n5--Logout")
        if user_role == 'admin':
            print("6--View Users\n7--Add Product\n8--Update Product\n9--Delete Product\n10--View All Transactions\n11--Inventory Notification\n12--Generate Sales Report\n13--Generate User Activity Report\n14--Generate Inventory Report\n15--Search and Filter Products\n16--Search and Filter Transactions")
        choice = input("Please choose an option: ")
        
        if choice == '1':
            view_profile(user_id)
        elif choice == '2':
            view_products(user_id)
        elif choice == '3':
            generate_bill(user_id)
        elif choice == '4':
            view_transactions(user_id)
        elif choice == '5':
            print("Logged out successfully.")
            break
        elif choice == '6' and user_role == 'admin':
            view_users()
        elif choice == '7' and user_role == 'admin':
            add_product()
        elif choice == '8' and user_role == 'admin':
            update_product()
        elif choice == '9' and user_role == 'admin':
            delete_product()
        elif choice == '10' and user_role == 'admin':
            view_all_transactions()
        elif choice == '11' and user_role == 'admin':
            inventory_notification()
        elif choice == '12' and user_role == 'admin':
            generate_sales_report()
        elif choice == '13' and user_role == 'admin':
            generate_user_activity_report()
        elif choice == '14' and user_role == 'admin':
            generate_inventory_report()
        elif choice == '15' and user_role == 'admin':
            search_filter_products()
        elif choice == '16' and user_role == 'admin':
            search_filter_transactions()
        else:
            print("Invalid choice. Please try again.")

