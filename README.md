# 🧾 Billing System Terminal Based

## 📋 Overview

Welcome to the **Billing System**! This terminal-based application is designed to efficiently manage users, products, transactions, and inventory. It includes role-based access control, ensuring that regular users and admins have access to appropriate functionalities. Built using Python and MySQL, this system is both robust and easy to use.

## ✨ Features

### For Users:

1. **👤 View Profile**: Access your personal profile information.
2. **🛍️ View Products**: Browse the list of available products.
3. **🧾 Generate Bill**: Create bills for your purchases.
4. **📄 View Transactions**: Review your transaction history.
5. **🚪 Logout**: Securely log out of the system.

### For Admins:

1. **👤 View Profile**: Access your personal profile information.
2. **🛍️ View Products**: Browse the list of available products.
3. **🧾 Generate Bill**: Create bills for purchases.
4. **📄 View Transactions**: Review your transaction history.
5. **🚪 Logout**: Securely log out of the system.
6. **👥 View Users**: See the list of all users.
7. **➕ Add Product**: Add new products to the inventory.
8. **✏️ Update Product**: Update details of existing products.
9. **❌ Delete Product**: Remove products from the inventory.
10. **🔍 View All Transactions**: View all user transactions.
11. **🔔 Inventory Notification**: Get alerts for low inventory.
12. **📊 Generate Sales Report**: Generate reports on sales.
13. **📝 Generate User Activity Report**: Generate reports on user activities.
14. **📦 Generate Inventory Report**: Generate reports on inventory status.
15. **🔎 Search and Filter Products**: Search and filter the product list.
16. **🔍 Search and Filter Transactions**: Search and filter transactions.

## 🗂️ Directory Structure

```plaintext
billing_system/
│
├── main.py
├── auth.py
├── user.py
├── product.py
├── transaction.py
├── report.py
├── inventory.py
└── search_filter.py
```

## ⚙️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/billing_system.git
   cd billing_system
   ```

2. **Install dependencies:**

   ```bash
   pip install tabulate mysql-connector-python
   ```

3. **Set up the database:**
   Create a MySQL database named billing_system and create the required tables using the following SQL commands:

   ```sql
   CREATE DATABASE IF NOT EXISTS billing_system;

   USE billing_system;

   CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password TEXT,
    name TEXT,
    address TEXT,
    age INT,
    role TEXT DEFAULT 'user'
   );


   CREATE TABLE IF NOT EXISTS products (
   id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(255) UNIQUE,
   price FLOAT,
   description TEXT,
   category TEXT,
   quantity INT DEFAULT 0
   );

   CREATE TABLE IF NOT EXISTS transactions (
   id INT AUTO_INCREMENT PRIMARY KEY,
   user_id INT,
   product_id INT,
   quantity INT,
   date DATETIME,
   FOREIGN KEY(user_id) REFERENCES users(id),
   FOREIGN KEY(product_id) REFERENCES products(id)
   );

   ```

## 🚀 Usage

1. **Run the application:**

```bash
python main.py
```

2. **Login or Register:**
   Upon running the application, you will be prompted to login or register as a new user.

3. **User Menu:**
   Based on your role (user or admin), you will be presented with a menu of options.

## 🛠️ Code Explanation

### main.py

This is the entry point of the application. It contains the `main` function which handles user login and redirects to the appropriate menu based on the user's role.

### auth.py

Contains authentication functions for user login and registration.

### user.py

Handles user-related functionalities, including viewing the user profile, viewing products, generating bills, viewing transactions, and user menu options. It imports necessary functions from other modules.

### product.py

Manages product-related functionalities, including viewing, adding, updating, and deleting products.

### transaction.py

Manages transaction-related functionalities, including generating bills and viewing transactions.

### report.py

Generates various reports, such as sales reports and user activity reports.

### inventory.py

Handles inventory-related functionalities, including inventory notifications and generating inventory reports. It includes an SMTP integration to automatically send email notifications when product stock falls below or equals 5.

### search_filter.py

Provides search and filter functionalities for products and transactions.

## .

📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- This project utilizes the [tabulate](https://pypi.org/project/tabulate/) library for displaying data in tabular format.
