from datetime import datetime
from src.utils import validate_non_empty_string, validate_positive_int, print_table
from src.data.adapter import save_data
from src.products import list_products

def register_sale(data):
    """Registers a new sale transaction."""
    print("\n--- Register Sale ---")
    list_products(data)
    
    product_id = validate_positive_int("\nEnter Product ID to sell: ")
    product = next((p for p in data["products"] if p["id"] == product_id), None)
    
    if not product:
        print("Error: Product not found.")
        return

    if product["stock"] <= 0:
        print("Error: Product is out of stock.")
        return

    quantity = validate_positive_int("Quantity: ")
    
    if quantity > product["stock"]:
        print(f"Error: Insufficient stock. Only {product['stock']} available.")
        return

    customer_name = validate_non_empty_string("Customer Name: ")
    
    # Calculate total
    total_price = product["price"] * quantity
    
    # Apply discount logic (example: 10% if quantity > 5)
    discount = 0.0
    if quantity > 5:
        discount = total_price * 0.10
        print(f"Bulk discount applied: -${discount:.2f}")
    
    final_price = total_price - discount

    # Update stock
    product["stock"] -= quantity

    # Record sale
    sale = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "customer": customer_name,
        "product_id": product_id,
        "product_title": product["title"],
        "quantity": quantity,
        "total": final_price,
        "discount": discount
    }
    
    data["sales"].append(sale)
    save_data(data)
    
    print(f"\nSale registered successfully!")
    print(f"Total: ${final_price:.2f}")

def list_sales(data):
    """Displays sales history."""
    sales = data.get("sales", [])
    if not sales:
        print("No sales recorded yet.")
        return

    headers = ["Date", "Customer", "Product", "Qty", "Total"]
    rows = [[s["date"], s["customer"], s["product_title"], s["quantity"], f"${s['total']:.2f}"] for s in sales]
    print_table(headers, rows)
