import sys
import os

# Add the project root to sys.path to allow imports from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data.adapter import load_data
from src.utils import clear_screen
from src.products import add_product, update_product, delete_product, list_products
from src.sales import register_sale, list_sales
from src.reports import get_top_selling_products, get_sales_by_author, calculate_revenue

def main_menu():
    data = load_data()
    
    while True:
        # clear_screen() # Optional: keep history visible for now
        print("\n=========================================")
        print("   BOOKSTORE MANAGEMENT SYSTEM")
        print("=========================================")
        print("1. Manage Inventory")
        print("2. Manage Sales")
        print("3. View Reports")
        print("4. Exit")
        
        choice = input("\nSelect an option: ")
        
        if choice == "1":
            inventory_menu(data)
        elif choice == "2":
            sales_menu(data)
        elif choice == "3":
            reports_menu(data)
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def inventory_menu(data):
    while True:
        print("\n--- Inventory Management ---")
        print("1. List Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            list_products(data)
        elif choice == "2":
            add_product(data)
        elif choice == "3":
            update_product(data)
        elif choice == "4":
            delete_product(data)
        elif choice == "5":
            break
        else:
            print("Invalid option.")

def sales_menu(data):
    while True:
        print("\n--- Sales Management ---")
        print("1. Register New Sale")
        print("2. View Sales History")
        print("3. Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            register_sale(data)
        elif choice == "2":
            list_sales(data)
        elif choice == "3":
            break
        else:
            print("Invalid option.")

def reports_menu(data):
    while True:
        print("\n--- Reports ---")
        print("1. Top Selling Products")
        print("2. Sales by Author")
        print("3. Financial Report")
        print("4. Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            get_top_selling_products(data)
        elif choice == "2":
            get_sales_by_author(data)
        elif choice == "3":
            calculate_revenue(data)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
