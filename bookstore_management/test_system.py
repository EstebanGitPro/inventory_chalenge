import sys
import os
import unittest
from unittest.mock import patch
import json

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data.adapter import load_data, save_data, DATA_FILE
from src.products import add_product
from src.sales import register_sale
from src.reports import calculate_revenue

class TestBookstoreSystem(unittest.TestCase):
    
    def setUp(self):
        # Reset data file for testing
        self.test_data = {
            "products": [
                {"id": 1, "title": "Test Book", "author": "Tester", "category": "Test", "price": 10.0, "stock": 10}
            ],
            "sales": []
        }
        save_data(self.test_data)
        self.data = load_data()

    def test_add_product(self):
        print("\nTesting Add Product...")
        inputs = ["New Book", "New Author", "Fiction", "20.0", "5"]
        with patch('builtins.input', side_effect=inputs):
            add_product(self.data)
        
        self.assertEqual(len(self.data["products"]), 2)
        self.assertEqual(self.data["products"][1]["title"], "New Book")
        print("Add Product: PASS")

    def test_register_sale(self):
        print("\nTesting Register Sale...")
        # Sell 2 copies of ID 1
        inputs = ["1", "2", "John Doe"] 
        with patch('builtins.input', side_effect=inputs):
            register_sale(self.data)
        
        self.assertEqual(len(self.data["sales"]), 1)
        self.assertEqual(self.data["sales"][0]["total"], 20.0)
        self.assertEqual(self.data["products"][0]["stock"], 8)
        print("Register Sale: PASS")

    def test_register_sale_discount(self):
        print("\nTesting Register Sale with Discount...")
        # Sell 6 copies of ID 1 (should trigger 10% discount)
        # Price 10 * 6 = 60. Discount 6. Total 54.
        inputs = ["1", "6", "Jane Doe"]
        with patch('builtins.input', side_effect=inputs):
            register_sale(self.data)
            
        self.assertEqual(self.data["sales"][0]["discount"], 6.0)
        self.assertEqual(self.data["sales"][0]["total"], 54.0)
        print("Discount Logic: PASS")

if __name__ == '__main__':
    unittest.main()
