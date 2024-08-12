# billing_system/inventory.py
import smtplib
from tabulate import tabulate
import mysql.connector as mysql
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Inventory notification function for admin
def inventory_notification():
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    c.execute("SELECT name, quantity FROM products WHERE quantity <= 5")
    low_stock_products = c.fetchall()
    if low_stock_products:
        print("\n--- Low Stock Products ---")
        for product in low_stock_products:
            print(f"Product: {product[0]}, Quantity: {product[1]}")
        # Send email notification
        send_email(low_stock_products)
    else:
        print("No low stock products.")
    conn.close()

# Function to send email using SMTP
def send_email(low_stock_products):
    from_email = "s.khan9430319425@gmail.com"
    to_email = "s.khan9430319425@gmail.com"
    subject = "Low Stock Alert"
    body = "The following products are low in stock:\n\n"
    
    for product in low_stock_products:
        body += f"Product: {product[0]}, Quantity: {product[1]}\n"
    
    # Create email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Establish connection to the Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Upgrade to secure connection
        
        # Login to your Gmail account (use App password for security)
        server.login(from_email, "epkjleiitfopyfbh")
        
        # Send email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("Low stock alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


# Generate inventory report function for admin
def generate_inventory_report():
    conn = mysql.connect(
        host="localhost",
        port="3306",
        username="root",
        password="",
        database ='billing_system'
    )
    c = conn.cursor()
    c.execute('''SELECT name, price, description, category, quantity 
                 FROM products''')
    inventory_report = c.fetchall()
    if inventory_report:
        print("\n--- Inventory Report ---")
        print(tabulate(inventory_report, headers=["Product Name", "Price", "Description", "Category", "Quantity"]))
    else:
        print("No inventory data available.")
    conn.close()

