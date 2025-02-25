from inventory.inventory_manager import InventoryManager

iv = InventoryManager()
RUN = True


def menu():
    """
    Main menu for the Inventory Management.
    Gets user input and forwards it to InventoryManager class.
    """
    print("What do you want to do?")
    print(
        "1. Add new product\n"
        "2. Remove an existing product\n"
        "3. Update the quantity of a product\n"
        "4. Update the price of a product\n"
        "5. Get info for a product\n"
        "6. Show total product value\n"
        "7. Show all products\n"
        "8. Save changes to database\n"
        "0. Exit"
    )
    #iv.menu_choice()
    try:
        user_input = int(input("Your choice: "))
    except ValueError:
        print(">>> Input out of range. Try again <<<\n")
    else:
        if user_input not in range(0, 9):
            print(">>> Input out of range. Try again <<<\n")
        elif user_input == 1:
            iv.add_product()
        elif user_input == 2:
            iv.remove_product()
        elif user_input == 3:
            iv.update_product_quantity()
        elif user_input == 4:
            iv.update_price()
        elif user_input == 5:
            iv.product_info()
        elif user_input == 6:
            iv.get_total_inventory_value()
        elif user_input == 7:
            iv.show_all_products()
        elif user_input == 8:
            iv.save_changes()
        elif user_input == 0:
            if input("Save changes before exit? (Y/N): ").lower() == "y":
                iv.save_changes()
            print("--- Exiting program. See you next time. ---")
            global RUN
            RUN = False


iv.load_changes()
while RUN:
    menu()
