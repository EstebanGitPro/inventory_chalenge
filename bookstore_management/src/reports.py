from src.utils import print_table

def get_top_selling_products(data):
    """Shows top 3 best-selling products."""
    sales = data.get("sales", [])
    if not sales:
        print("No sales data available.")
        return

    # Aggregate sales by product
    product_sales = {}
    for sale in sales:
        pid = sale["product_id"]
        qty = sale["quantity"]
        product_sales[pid] = product_sales.get(pid, 0) + qty

    # Sort by quantity desc
    sorted_sales = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:3]

    print("\n--- Top 3 Best-Selling Products ---")
    headers = ["Rank", "Product", "Total Sold"]
    rows = []
    
    for rank, (pid, qty) in enumerate(sorted_sales, 1):
        # Find product name
        product = next((p for p in data["products"] if p["id"] == pid), None)
        title = product["title"] if product else "Unknown Product"
        rows.append([rank, title, qty])
        
    print_table(headers, rows)

def get_sales_by_author(data):
    """Shows total sales grouped by author."""
    sales = data.get("sales", [])
    products = data.get("products", [])
    
    if not sales:
        print("No sales data available.")
        return

    author_sales = {}
    
    for sale in sales:
        pid = sale["product_id"]
        product = next((p for p in products if p["id"] == pid), None)
        if product:
            author = product["author"]
            author_sales[author] = author_sales.get(author, 0) + sale["total"]

    print("\n--- Sales by Author ---")
    headers = ["Author", "Total Revenue"]
    rows = [[author, f"${total:.2f}"] for author, total in author_sales.items()]
    print_table(headers, rows)

def calculate_revenue(data):
    """Calculates net and gross revenue."""
    sales = data.get("sales", [])
    
    gross_revenue = sum(s["total"] + s["discount"] for s in sales)
    net_revenue = sum(s["total"] for s in sales)
    total_discounts = sum(s["discount"] for s in sales)

    print("\n--- Financial Report ---")
    print(f"Gross Revenue (before discounts): ${gross_revenue:.2f}")
    print(f"Total Discounts Given:            -${total_discounts:.2f}")
    print(f"Net Revenue (actual income):      ${net_revenue:.2f}")
