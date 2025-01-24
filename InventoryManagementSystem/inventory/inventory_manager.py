import json 



with open("product.json", "r") as f:
    products = json.load(f)
    
products["dishwasher"]["price"] = 250

print(products["dishwasher"]["price"])



print("New price for 'dishwasher':", products["dishwasher"]["price"])