# billing_system/auth.py
import sqlite3
from hashlib import sha256
from user import user_menu

def hash_password(password):
    return sha256(password.encode()).hexdigest()

# def signup():
#     print("\n--- Signup ---")
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     name = input("Enter name: ")
#     address = input("Enter address: ")
#     age = int(input("Enter age: "))
    
#     conn = sqlite3.connect('billing_system.db')
#     c = conn.cursor()
#     try:
#         c.execute("INSERT INTO users (username, password, name, address, age) VALUES (?, ?, ?, ?, ?)",
#                   (username, hash_password(password), name, address, age))
#         conn.commit()
#         print("User successfully signed up.")
#     except sqlite3.IntegrityError:
#         print("Username already exists. Please choose a different username.")
#     conn.close()

# Signup function with role input
def signup():
    print("\n--- Signup ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    age = input("Enter your age: ")
    role = input("Enter role (user/admin): ")

    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    hashed_password = hash_password(password)
    try:
        c.execute("INSERT INTO users (username, password, name, address, age, role) VALUES (?, ?, ?, ?, ?, ?)", 
                  (username, hashed_password, name, address, age, role))
        conn.commit()
        print("Signup successful! Please proceed to login.")
        login()
    except sqlite3.IntegrityError:
        print("Username already exists. Please try a different one.")
    conn.close()


# Login function
def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    c.execute("SELECT id, password, role FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    if user and user[1] == hash_password(password):
        print("Login successful!")
        user_id = user[0]
        user_role = user[2]
        user_menu(user_id, user_role)
    else:
        print("Invalid username or password. Please try again.")
    conn.close()


