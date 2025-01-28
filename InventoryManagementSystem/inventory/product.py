#products = {}

class Product:
    def __init__(self, name, price, quantity):
        self.name = name         
        self.price = price        
        self.quantity = quantity  

    def update_quantity(self, quantity):
        self.quantity = quantity  

    def update_price(self, price):
        self.price = price       

    def get_product_info(self):
        
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    