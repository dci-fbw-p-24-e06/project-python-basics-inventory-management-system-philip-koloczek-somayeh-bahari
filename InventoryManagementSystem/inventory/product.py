class Product:
    def __init__(self, price: float, quantity: int):
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product(price={self.price}, quantity={self.quantity})"

    def __str__(self):
        return f"Price: ${self.price}, Quantity: {self.quantity}, Value: ${self.get_value()}"  # noqa

    def update_quantity(self, new_quantity: int):
        """Takes new quantity as input and sets it as new value for quantity"""
        self.quantity = new_quantity

    def update_price(self, new_price: int):
        """Takes new price as input and sets it as new value for price"""
        self.price = new_price

    def get_value(self):
        """Returns the result of price * quantity"""
        return self.price * self.quantity

    def to_dict(self):
        """Returns a dictionary to save to json"""
        return {
            "price": self.price,
            "quantity": self.quantity
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Product object from a dictionary"""
        return cls(
            price = data["price"],  # noqa
            quantity = data["quantity"]  # noqa
        )
