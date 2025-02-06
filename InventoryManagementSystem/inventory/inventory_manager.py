

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

from .product import Product
import json

class InventoryManager:
    def __init__(self):
        self.products = {}
        self.load_changes()

    def add_product(self):
        product_name = input("Input new product name: ")
        if product_name not in self.products:
            product_price = int(input("Input product price: $"))
            product_quantity = int(input("Input quantity: "))        
            self.products[product_name] = Product(product_price, product_quantity)
            print(">>> Product added")
            self.save_changes() # add to list after adding
        else:
            print(">>> Product name already in use. Process aborted.\n")
        
    def remove_product(self):
        p_name = input("Input product to remove: ")
        if p_name in self.products:
            del self.products[p_name]
            self.save_changes() # save change 
            print(f">>> {p_name} removed from product list\n")
        else:
            print(f">>>{p_name} not in database. Process aborted.\n")

    def update_product_quantity(self):
        p_name = input("Insert product name?: ")
        n_quant = int(input(f"Current quantity: {self.products[p_name].quantity}. Insert new quantity: "))
        if p_name in self.products:
            self.products[p_name].update_quantity(n_quant)
            self.save_changes() #save update
            print(f">>> Quantity of {p_name} updated to {n_quant}.\n")
        else:
            print(f">>> {p_name} not in database. Process aborted.\n")

    def update_price(self):
        p_name = input("Insert product name: ")
        n_price = int(input(f"Current price: ${self.products[p_name].price}. Insert new price: $"))
        if p_name in self.products:
            self.products[p_name].update_price(n_price)
            self.save_changes() # save update price
            print(f">>> Price of {p_name} updated to {n_price}.\n")
        else:
            print(f">>> {p_name} not in database. Process aborted.\n")

    def product_info(self):
        user_choice = input("Insert product name: ")
        if user_choice in self.products:
            print(f"\nProduct name: {user_choice} {self.products[user_choice].__repr__()}\n")
        else:
            print(">>> Product not found.\n")
    
    def show_all_products(self):
        n = 0
        if self.products:
            for product in self.products:
                n += 1
                print(f"{n}. Product name: {product} {self.products[product].__repr__()}")
        else:
            print(">>> No products in inventory\n")


    def get_total_inventory_value(self):
        total_value = 0
        n = 0
        for product in self.products:
            total_value += self.products[product].get_value()
            n += 1
        print(f"\nYou have {n} products in your database with a total value of: ${total_value}.\n")

    # def save_changes(self):
    #     with open("inventory.products.json", "w") as database:
    #         json.dump(self.products, database, indent=4)
    
    def save_changes(self):
        try:
            with open("InventoryManagementSystem/inventory/product.py", "w") as database:
                json.dump(self.products, database, default=str, indent=4)
                print(">>> Changes saved successfully.")

        except Exception as e:
            print(f"Error saving changes: {e}")
        
        #     for product_name, product in self.products.items():
        #         data[product_name] = {'price': product.price, 'quantity': product.quantity}
        # json.dump(data, database, indent=4)
        # print(">>> Changes saved to file.")

    # def load_changes(self):
    #     try:
    #         with open("products.json", "w") as database:
    #             json.dump(self.products, database, indent=4)

    def load_changes(self):
        try:
            with open("InventoryManagementSystem/inventory/product.py", "r") as database:
                self.product = json.load(database)
            
            # for product_name, details in data.items():
            #     self.products[product_name] = Product(details['price'], details['quantity'])
            print(">>> Products loaded successfully from file.")
        except FileNotFoundError:
            print(">>> No saved products found. Starting fresh.")

        except json.JSONDecodeError:
            print(">>> Error loading inventory data. The file may be corrupted.")
        except Exception as e:
            print(f"Error loading inventory: {e}")

""" class InventoryManager:
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
        else:
                return "Product not found"

    def get_total_inventory_value(self):
        total_value = 0
        for product in self.products.values():
            total_value += product.price * product.quantity
        return total_value """

