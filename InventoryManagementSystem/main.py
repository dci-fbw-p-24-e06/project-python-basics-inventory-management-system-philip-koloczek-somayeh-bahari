from inventory.inventory_manager import InventoryManager

iv = InventoryManager()

run = True

def menu():
    print("What do you want to do?")
    print("1. Add new product\n2. Remove an existing product\n3. Update the quantity of a product\n4. Get info for a product\n5. Show total product value\n6. Show all products")
    user_input = int(input("Your choice: "))
    if user_input not in range(0,7):
        print("Input out of range. Try again\n")
        menu()
    if user_input == 1:
        iv.add_product()
    elif user_input == 2:
        iv.remove_product()
    elif user_input == 3:
        iv.update_product_quantity()
    elif user_input == 4:
        iv.product_info()
    elif user_input == 5:
        iv.get_total_inventory_value()
    elif user_input == 6:
        iv.show_all_products()
    elif user_input == 0:
        global run
        run = False

while run:
    menu()