# billing_system/db_utils.py
import sqlite3



# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('billing_system.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    name TEXT,
                    address TEXT,
                    age INTEGER,
                    role TEXT DEFAULT 'user'
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE,
                    price REAL,
                    description TEXT,
                    category TEXT,
                    quantity INTEGER DEFAULT 0
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER,
                    date TEXT,
                    FOREIGN KEY(user_id) REFERENCES users(id),
                    FOREIGN KEY(product_id) REFERENCES products(id)
                )''')
    conn.commit()
    conn.close()

# Other utility functions can be added as needed
