from .product import Product
import json

class InventoryManager:
    def __init__(self):
        self.products = {}
        

    def add_product(self):
        p_name: str = input("Input new product name: ")
        if p_name not in self.products:
            p_price = False
            while not p_price:
                try:
                    p_price: float = float(input("Input product price: $"))
                except ValueError:
                    print("No valid input. Please use only numbers and the . as separator: $")
            p_quantity = False
            while not p_quantity:
                try:
                    p_quantity: int = int(input("Input quantity: "))
                except ValueError:
                    print("No valid input. Please use only numbers")        
            self.products[p_name] = Product(p_price, p_quantity)
            print(f">>> Product added: {p_name} -> {self.products[p_name].__str__()}")
            #self.save_changes() # add to list after adding
        else:
            print(">>> Product name already in use. Process aborted.\n")
        
    def remove_product(self):
        p_name = input("Input product to remove: ")
        if p_name in self.products:
            del self.products[p_name]
            #self.save_changes() # save change 
            print(f">>> {p_name} removed from product list\n")
        else:
            print(f">>>{p_name} not in database. Process aborted.\n")

    def update_product_quantity(self):
        p_name = input("Insert product name?: ")
        if p_name in self.products:
            n_quant = False
            while not n_quant:
                try:
                    n_quant = int(input(f"Current quantity: {self.products[p_name].quantity}. Insert new quantity: "))
                except ValueError:
                    print("No valid input. Please use only numbers")
            self.products[p_name].update_quantity(n_quant)
            #self.save_changes() #save update
            print(f">>> Quantity of {p_name} updated to {n_quant}.\n")
        else:
            print(f">>> {p_name} not in database. Process aborted.\n")

    def update_price(self):
        p_name = input("Insert product name: ")
        if p_name in self.products:
            n_price = False
            while not n_price:
                try:
                    n_price = int(input(f"Current price: ${self.products[p_name].price}. Insert new price: $"))
                except ValueError:
                    print("No valid input. Please use only numbers and the . as separator: $")
            self.products[p_name].update_price(n_price)
            #self.save_changes() # save update price
            print(f">>> Price of {p_name} updated to {n_price}.\n")
        else:
            print(f">>> {p_name} not in database. Process aborted.\n")

    def product_info(self):
        user_choice = input("Insert product name: ")
        if user_choice in self.products:
            print(f"\nProduct name: {user_choice} {self.products[user_choice].__str__()}\n")
        else:
            print(">>> Product not found.\n")
    
    def show_all_products(self):
        n = 0
        if self.products:
            for product in self.products:
                n += 1
                print(f"{n}. Product name: {product} {self.products[product].__str__()}")
            print("\n")
        else:
            print(">>> No products in inventory\n")


    def get_total_inventory_value(self):
        total_value: float = 0
        n: int = 0
        for product in self.products:
            total_value += self.products[product].get_value()
            n += 1
        print(f"\nYou have {n} products in your database with a total value of: ${total_value}.\n")


    def save_changes(self):
        try:
            data = {name: product.to_dict() for name, product in self.products.items()}
            with open("InventoryManagementSystem/inventory/products.json", "w") as database:
                json.dump(data, database, default=dict, indent=4)
                print(">>> Changes saved successfully.")

        except Exception as e:
            print(f"Error saving changes: {e}")
        
     

    def load_changes(self):
        try:
            with open("InventoryManagementSystem/inventory/products.json", "r") as database:
                data = json.load(database)
                self.products = {name : Product.from_dict(details) for name, details in data.items()}
            
            print(">>> Products loaded successfully from file.")
        except FileNotFoundError:
            print(">>> No saved products found. Starting fresh.")

        except json.JSONDecodeError:
            print(">>> Error loading inventory data. The file may be corrupted.")
        except Exception as e:
            print(f"Error loading inventory: {e}")
   
