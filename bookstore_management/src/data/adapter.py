import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'store_data.json')

DEFAULT_DATA = {
    "products": [
        {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Classic", "price": 10.99, "stock": 50},
        {"id": 2, "title": "1984", "author": "George Orwell", "category": "Dystopian", "price": 8.99, "stock": 30},
        {"id": 3, "title": "Python Crash Course", "author": "Eric Matthes", "category": "Education", "price": 25.50, "stock": 20},
        {"id": 4, "title": "Clean Code", "author": "Robert C. Martin", "category": "Education", "price": 32.00, "stock": 15},
        {"id": 5, "title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy", "price": 12.50, "stock": 40}
    ],
    "sales": []
}

def load_data():
    """Loads data from the JSON file. Creates it with defaults if missing."""
    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Fallback if file is corrupted
        return DEFAULT_DATA

def save_data(data):
    """Saves the data dictionary to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")
