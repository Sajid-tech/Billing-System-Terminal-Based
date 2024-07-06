# billing_system/main.py
from auth import signup, login
from db_utils import init_db

def main():
    init_db()
    while True:
        print("\n--- Billing System ---")
        print("1--Signup\n2--Login\n3--Exit")
        choice = input("Please choose an option: ")
        
        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the billing system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
