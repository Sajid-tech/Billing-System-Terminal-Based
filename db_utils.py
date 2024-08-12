# billing_system/db_utils.py
import mysql.connector as mysql



# Initialize the SQLite database
def init_db():
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    # Create the database if it doesn't exist
    c.execute("CREATE DATABASE IF NOT EXISTS billing_system")


    

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE,
                    password TEXT,
                    name TEXT,
                    address TEXT,
                    age INT,
                    role TEXT DEFAULT 'user'
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS products (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) UNIQUE,
                    price FLOAT,
                    description TEXT,
                    category TEXT,
                    quantity INT DEFAULT 0
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT,
                    product_id INT,
                    quantity INT,
                    date DATETIME,
                    FOREIGN KEY(user_id) REFERENCES users(id),
                    FOREIGN KEY(product_id) REFERENCES products(id)
                )''')
    conn.commit()
    conn.close()

# Other utility functions can be added as needed
