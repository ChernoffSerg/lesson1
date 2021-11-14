from pprint import pprint  # визуально форматирует вывод

product = {
    "name": "iPhone 12",
    "stock": 24,
    "price": 65432.1
}

pprint(product)
phones = ["Samsung Galaxy S21", "iPhone 12"]
product["recomended"] = phones
pprint(product)