

# # products dictionary
# #from product import products
# import json 


# def readProducts():
#     with open("InventoryManagementSystem/inventory/products.json", 'r') as file:
#         products = json.load(file)
#     return products
# readProducts()

# def writeProducts(products):
#     with open("InventoryManagementSystem/inventory/products.json", 'w') as file:
#         json.dump(products,file, indent=4)
#     print(products)

# def inventory():
#     """
#     A simple inventory management system that allows the user to:
#     1. Add a new product.
#     2. Remove an existing product.
#     3. Update product details (name or price).
#     4. Update product quantities.
#     5. Retrieve information about a product.
#     6. Calculate the total value of all products in the inventory.
#     """
#     products = readProducts()

#     # loop to interact with the user
#     while True:
#         print("\n--- Inventory Management ---")
#         print("1. Add Product")
#         print("2. Remove Product")
#         print("3. Update Product")
#         print("4. Update Quantities")
#         print("5. Retrieve Product Information")
#         print("6. Calculate Total Value")
#         print("7. Exit")
        
#         # get the user's choice
#         choice = input("Enter your choice (1-7): ")
#         #readProducts()

#         if choice == "1":
#             #  Add Product
#             product_id = input("Enter product ID: ")
#             name = input("Enter product name: ")
#             price = float(input("Enter product price: "))
#             quantity = int(input("Enter product quantity: "))
#             #products.update(product_id)
#             products.update({product_id : {"name": name, "price": price, "quantity": quantity}})
#             print(f"Product {name} added successfully!")

#         elif choice == "2":
#             # Remove Product
#             product_id = input("Enter product ID to remove: ")
#             if product_id in products:
#                 del products[product_id]
#                 print("Product removed successfully!")
#             else:
#                 print("Product not found!")

#         elif choice == "3":
#             # Update Product
#             product_id = input("Enter product ID to update: ")
#             if product_id in products:
#                 new_name = input("Enter new name : ")
#                 new_price = input("Enter new price : ")
#                 if new_name:
#                     products[product_id]["name"] = new_name
#                 if new_price:
#                     products[product_id]["price"] = float(new_price)
#                 print("Product updated successfully!")
#             else:
#                 print("Product not found!")

#         elif choice == "4":
#             # Update Quantities
#             product_id = input("Enter product ID to update quantity: ")
#             if product_id in products:
#                 new_quantity = int(input("Enter new quantity: "))
#                 products[product_id]["quantity"] = new_quantity
#                 print("Product quantity updated successfully!")
#             else:
#                 print("Product not found!")

#         elif choice == "5":
#             # Retrieve Product Information
#             product_id = input("Enter product ID to retrieve information: ")
#             if product_id in products:
#                 product = products[product_id]
#                 print(f"Product ID: {product_id}")
#                 print(f"Name: {product['name']}")
#                 print(f"Price: {product['price']}")
#                 print(f"Quantity: {product['quantity']}")
#             else:
#                 print("Product not found!")

#         elif choice == "6":
#             # Calculate Total Value
#             for p in products.values():
#                 total_value = sum(p["price"] * p["quantity"])
#                 print(f"The total value of inventory is: {total_value}") 

#         elif choice == "7":
#             # Exit
#             print("Exiting program. Goodbye!")
#             break

#         else:
#             print("Invalid choice! Please try again.")

#         writeProducts(products)

# #inventory()
# #print(readProducts())

#from product import *

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]

    def update_product_quantity(self, product_name, quantity):
        if product_name in self.products:
            self.products[product_name].update_quantity(quantity)

    def get_product_info(self, product_name):
        if product_name in self.products:
            return self.products[product_name].get_product_info()
        return "Product not found"

    def get_total_inventory_value(self):
        total_value = 0
        for product in self.products.values():
            total_value += product.price * product.quantity
        return total_value
