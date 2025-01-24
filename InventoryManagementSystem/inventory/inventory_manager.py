from product import products

products["dishwasher"]["price"] = 250

print(products["dishwasher"]["price"])

with open("product.py", "w") as p:
    p.write("products = " + repr(products) + "\n")

print("New price for 'dishwasher':", products["dishwasher"]["price"])