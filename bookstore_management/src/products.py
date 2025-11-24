from src.utils import validate_non_empty_string, validate_positive_int, print_table
from src.data.adapter import save_data

def list_products(data):
    """Displays all products in a table."""
    products = data.get("products", [])
    if not products:
        print("No products found.")
        return

    headers = ["ID", "Title", "Author", "Category", "Price", "Stock"]
    rows = [[p["id"], p["title"], p["author"], p["category"], f"${p['price']:.2f}", p["stock"]] for p in products]
    print_table(headers, rows)

def add_product(data):
    """Adds a new product to the inventory."""
    print("\n--- Add New Product ---")
    title = validate_non_empty_string("Title: ")
    author = validate_non_empty_string("Author: ")
    category = validate_non_empty_string("Category: ")
    
    while True:
        try:
            price = float(input("Price: "))
            if price < 0:
                print("Price must be positive.")
                continue
            break
        except ValueError:
            print("Invalid price.")

    stock = validate_positive_int("Initial Stock: ")

    # Generate new ID
    products = data["products"]
    new_id = max([p["id"] for p in products], default=0) + 1

    new_product = {
        "id": new_id,
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "stock": stock
    }

    products.append(new_product)
    save_data(data)
    print(f"Product '{title}' added successfully with ID {new_id}.")

def update_product(data):
    """Updates an existing product's stock or price."""
    list_products(data)
    product_id = validate_positive_int("\nEnter Product ID to update: ")
    
    product = next((p for p in data["products"] if p["id"] == product_id), None)
    if not product:
        print("Product not found.")
        return

    print(f"Updating '{product['title']}'")
    print("1. Update Price")
    print("2. Update Stock")
    choice = input("Choose option: ")

    if choice == "1":
        while True:
            try:
                new_price = float(input("New Price: "))
                if new_price < 0:
                    print("Price must be positive.")
                    continue
                product["price"] = new_price
                break
            except ValueError:
                print("Invalid price.")
    elif choice == "2":
        new_stock = validate_positive_int("New Stock Quantity: ")
        product["stock"] = new_stock
    else:
        print("Invalid option.")
        return

    save_data(data)
    print("Product updated successfully.")

def delete_product(data):
    """Removes a product from inventory."""
    list_products(data)
    product_id = validate_positive_int("\nEnter Product ID to delete: ")
    
    product = next((p for p in data["products"] if p["id"] == product_id), None)
    if not product:
        print("Product not found.")
        return

    confirm = input(f"Are you sure you want to delete '{product['title']}'? (yes/no): ").lower()
    if confirm == "yes":
        data["products"].remove(product)
        save_data(data)
        print("Product deleted.")
    else:
        print("Deletion cancelled.")
