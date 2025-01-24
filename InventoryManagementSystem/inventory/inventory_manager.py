import json 


with open("/home/philip/projects/project-python-basics-inventory-management-system-philip-koloczek-somayeh-bahari/InventoryManagementSystem/inventory/product.json", "r") as f:
    products = json.load(f)

# Änderungen vornehmen
products["dishwasher"]["price"] = 160

# Ergebnis anzeigen
print(products["dishwasher"]["price"])

with open("/home/philip/projects/project-python-basics-inventory-management-system-philip-koloczek-somayeh-bahari/InventoryManagementSystem/inventory/product.json", "w") as f:
    json.dump(products, f, indent=4)


print("New price for 'dishwasher':", products["dishwasher"]["price"])