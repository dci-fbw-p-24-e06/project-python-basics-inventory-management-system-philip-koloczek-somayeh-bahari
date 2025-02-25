from .product import Product
import json


class InventoryManager:
    def __init__(self):
        self.products = {}

    def menu_choice(self):
        """Not active right now"""
        try:
            user_input = int(input("Your choice: "))
        except ValueError:
            print(">>> Input out of range. Try again <<<\n")
        else:
            if user_input not in range(0, 9):
                print(">>> Input out of range. Try again <<<\n")
            elif user_input == 1:
                self.add_product()
            elif user_input == 2:
                self.remove_product()
            elif user_input == 3:
                self.update_product_quantity()
            elif user_input == 4:
                self.update_price()
            elif user_input == 5:
                self.product_info()
            elif user_input == 6:
                self.get_total_inventory_value()
            elif user_input == 7:
                self.show_all_products()
            elif user_input == 8:
                self.save_changes()
            elif user_input == 0:
                self.end_program()
                
    def end_program(self):
        """Not working right now"""
        if input("Save changes before exit? (Y/N): ").lower() == "y":
            self.save_changes()
        print("--- Exiting program. See you next time. ---")
        run = False
        return run

    def add_product(self):
        """
        Takes product name as first input.
        Takes price as second input.
        Takes quantity as third input.
        Adds product to the products dictionary.
        Print out message.
        """
        p_name: str = input("Input new product name: ")
        if p_name not in self.products:
            p_price = False
            while not p_price:
                try:
                    p_price: float = float(input("Input product price: $"))
                except ValueError:
                    print("No valid input. Please use only numbers and the . as separator: $")  # noqa
            p_quantity = False
            while not p_quantity:
                try:
                    p_quantity: int = int(input("Input quantity: "))
                except ValueError:
                    print("No valid input. Please use only numbers")        
            self.products[p_name] = Product(p_price, p_quantity)
            print(f">>> Product added: {p_name} -> {self.products[p_name].__str__()}")  # noqa
        else:
            print(">>> Product name already in use. Process aborted.\n")

    def remove_product(self):
        """
        Takes product name as input.
        Removes product from products dictionary.
        """
        p_name = input("Input product to remove: ")
        if p_name in self.products:
            del self.products[p_name]
            print(f">>> {p_name} removed from product list\n")
        else:
            print(f">>>{p_name} not in database. Process aborted.\n")

    def update_product_quantity(self):
        """
        Takes product name as first input.
        Takes new quantity as second input.
        Prints out message.
        """
        p_name = input("Insert product name: ")
        if p_name in self.products:
            n_quant = False
            while not n_quant:
                try:
                    n_quant = int(input(f"Current quantity: {self.products[p_name].quantity}. Insert new quantity: "))  # noqa
                except ValueError:
                    print("No valid input. Please use only numbers")
            self.products[p_name].update_quantity(n_quant)
            print(f">>> Quantity of {p_name} updated to {n_quant}.\n")
        else:
            print(f">>> {p_name} not in database. Process aborted.\n")

    def update_price(self):
        """
        Takes product name as first input.
        Takes new price as second input.
        Prints out message.
        """
        p_name = input("Insert product name: ")
        if p_name in self.products:
            n_price = False
            while not n_price:
                try:
                    n_price = int(input(f"Current price: $ {self.products[p_name].price}. Insert new price: $"))  # noqa
                except ValueError:
                    print("No valid input. Please use only numbers and the . as separator: $")  # noqa
            self.products[p_name].update_price(n_price)
            print(f">>> Price of {p_name} updated to {n_price}.\n")
        else:
            print(f">>> {p_name} not in database. Process aborted.\n")

    def product_info(self):
        """
        Takes product name as input.
        Prints out message.
        """
        user_choice = input("Insert product name: ")
        if user_choice in self.products:
            print(f"\nProduct name: {user_choice} {self.products[user_choice].__str__()}\n")  # noqa
        else:
            print(">>> Product not found.\n")

    def show_all_products(self):
        """
        Takes no input.
        Prints out all the products in the database with name, amount,
        price and total value.
        """
        n = 0
        if self.products:
            for product in self.products:
                n += 1
                print(f"{n}. Product name: {product} {self.products[product].__str__()}")  # noqa
            print("\n")
        else:
            print(">>> No products in inventory\n")

    def get_total_inventory_value(self):
        """
        Prints out the number of products and their total value.
        Returns the total value as int.
        """
        total_value: float = 0
        n: int = 0
        for product in self.products:
            total_value += self.products[product].get_value()
            n += 1
        print(f"\nYou have {n} products in your database with a total value of: ${total_value}.\n") # noqa
        return total_value

    def save_changes(self):
        """Saves all changes from products dictionary to the products.json"""
        try:
            data = {name: product.to_dict() for name, product in self.products.items()}  # noqa
            with open("inventory/products.json", "w") as database:  # noqa
                json.dump(data, database, default=dict, indent=4)
                print(">>> Changes saved successfully.")

        except Exception as e:
            print(f"Error saving changes: {e}")

    def load_changes(self):
        """Loads all data from the products.json into products dictionary."""
        try:
            with open("inventory/products.json", "r") as database:  # noqa
                data = json.load(database)
                self.products = {name: Product.from_dict(details) for name, details in data.items()}  # noqa
            print(">>> Products loaded successfully from file.")
        except FileNotFoundError:
            print(">>> No saved products found. Starting fresh.")

        except json.JSONDecodeError:
            print(">>> Error loading inventory data. The file may be corrupted.")  # noqa
        except Exception as e:
            print(f"Error loading inventory: {e}")
