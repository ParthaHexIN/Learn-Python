products = {
    "Laptop": 65000,
    "Phone": 35000,
    "Tablet": 28000,
    "Monitor": 18000
}

highest_product = max(products, key=products.get)

print("Product:", highest_product)
print("Price:", products[highest_product])