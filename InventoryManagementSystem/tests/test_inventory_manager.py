from inventory.inventory_manager import InventoryManager
from inventory.product import Product
import unittest
from unittest.mock import patch


class TestInventoryManager(unittest.TestCase):

    @patch("builtins.input", side_effect=["hose", "34", "23"])
    def test_add_product(self, mock_input):

        iv = InventoryManager()
        iv.add_product()

        self.assertIn("hose", iv.products)
        self.assertEqual(iv.products["hose"].price, 34)
        self.assertEqual(iv.products["hose"].quantity, 23)
        print(">>> Test for adding product passed.")

    @patch("builtins.input", side_effect=["hose"])
    def test_remove_product(self, mock_input):

        iv = InventoryManager()
        iv.products['hose'] = Product(34, 23)
        iv.remove_product()

        self.assertNotIn("hose", iv.products)
        print(">>> Test for removing product passed.")

    @patch("builtins.input", side_effect=["hose", "50"])
    def test_update_product_quantity(self, mock_input):

        iv = InventoryManager()
        iv.products["hose"] = Product(34, 23)
        iv.update_product_quantity()

        self.assertEqual(iv.products["hose"].quantity, 50)
        print(">>> Test for updating product passed.")

    @patch("builtins.input", side_effect=["hose", "50"])
    def test_update_product_price(self, mock_input):

        iv = InventoryManager()
        iv.products["hose"] = Product(34, 23)
        iv.update_price()

        self.assertEqual(iv.products["hose"].quantity, 50)
        print(">>> Test for updating product price passed.")

    def test_get_total_inventory_value(self):
        iv = InventoryManager()
        iv.products['hose'] = Product(34, 23)
        iv.products['jacke'] = Product(345, 3)
        iv.products['tasche'] = Product(23.0, 22)

        total_value = iv.get_total_inventory_value()

        self.assertEqual(total_value, ((34 * 23) + (345 * 3) + (23.0 * 22)))
        print(">>> Test for getting total inventory value passed.")

    @patch('inventory.inventory_manager.InventoryManager.load_changes')
    def test_load_changes(self, mock_load_changes):        
        iv = InventoryManager()

        mock_load_changes.return_value = None
        iv.load_changes()
        mock_load_changes.assert_called_once()
        print(">>> Test for loading changes passed.")


if __name__ == '__main__':
    unittest.main()
