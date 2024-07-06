# Billing System

## Overview

This billing system is a terminal-based application designed to manage users, products, transactions, and inventory. It includes role-based access control, with different functionalities available to regular users and admins. The system is built using Python and SQLite for database management.

## Features

### For Users:

1. **View Profile**: Users can view their profile information.
2. **View Products**: Users can view the list of available products.
3. **Generate Bill**: Users can generate bills for purchased products.
4. **View Transactions**: Users can view their transaction history.
5. **Logout**: Users can log out of the system.

### For Admins:

1. **View Profile**: Admins can view their profile information.
2. **View Products**: Admins can view the list of available products.
3. **Generate Bill**: Admins can generate bills for purchased products.
4. **View Transactions**: Admins can view their transaction history.
5. **Logout**: Admins can log out of the system.
6. **View Users**: Admins can view the list of all users.
7. **Add Product**: Admins can add new products to the inventory.
8. **Update Product**: Admins can update existing product details.
9. **Delete Product**: Admins can delete products from the inventory.
10. **View All Transactions**: Admins can view all user transactions.
11. **Inventory Notification**: Admins receive notifications about low inventory.
12. **Generate Sales Report**: Admins can generate sales reports.
13. **Generate User Activity Report**: Admins can generate user activity reports.
14. **Generate Inventory Report**: Admins can generate inventory reports.
15. **Search and Filter Products**: Admins can search and filter products.
16. **Search and Filter Transactions**: Admins can search and filter transactions.

## Directory Structure

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

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/billing_system.git
   cd billing_system
   ```

2. **Install dependencies:**

   ```bash
   pip install tabulate
   ```

3. **Set up the database:**
   Create a SQLite database named `billing_system.db` and create the required tables using the following SQL commands:

   ```sql
   CREATE TABLE users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT NOT NULL,
       password TEXT NOT NULL,
       name TEXT,
       address TEXT,
       age INTEGER,
       role TEXT NOT NULL
   );

   CREATE TABLE products (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       price REAL NOT NULL,
       description TEXT,
       category TEXT,
       quantity INTEGER NOT NULL
   );

   CREATE TABLE transactions (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       user_id INTEGER NOT NULL,
       product_id INTEGER NOT NULL,
       quantity INTEGER NOT NULL,
       total_price REAL NOT NULL,
       FOREIGN KEY (user_id) REFERENCES users (id),
       FOREIGN KEY (product_id) REFERENCES products (id)
   );
   ```

## Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Login or Register:**
   Upon running the application, you will be prompted to login or register as a new user.

3. **User Menu:**
   Based on your role (user or admin), you will be presented with a menu of options.

## Code Explanation

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

Handles inventory-related functionalities, including inventory notifications and generating inventory reports.

### search_filter.py

Provides search and filter functionalities for products and transactions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project utilizes the [tabulate](https://pypi.org/project/tabulate/) library for displaying data in tabular format.
