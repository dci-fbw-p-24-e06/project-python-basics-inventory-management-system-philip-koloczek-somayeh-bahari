from inventory.inventory_manager import InventoryManager as im
from inventory.product import Product
import unittest


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.inventory_manager = im()
        self.product1 = Product(12,25)
        self.product2 = Product(14,35)
    def test_add_product(self):
        self.inventory_manager.add_product(self.product1)
        self.assertIn(12,self.inventory_manager.products)
    


