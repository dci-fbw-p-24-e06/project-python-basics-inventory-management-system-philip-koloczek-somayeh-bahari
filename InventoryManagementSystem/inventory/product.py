class Product:
    def __init__(self, price, quantity):
             
        self.price = price        
        self.quantity = quantity
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity  

    def update_price(self, new_price):
        self.price = new_price 

    def get_value(self):
        return self.price * self.quantity      

    def get_product_info(self):
        
        return f"Price: ${self.price}, Quantity: {self.quantity}, Total Value: ${self.get_value()}"








""" class Product:
    def __init__(self, name, price, quantity):
        self.name = name         
        self.price = price        
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity  

    def update_price(self, new_price):
        self.price = new_price       

    def get_product_info(self):
        
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}" """
    