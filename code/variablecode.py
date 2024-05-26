print("John")
name = "Ela"
middlename = "Na"
surname = "Fame"
print(name, middlename, surname)
print(name)
print(middlename)
print(surname)
quantity_of_pet_supplies = 10
price_per_unit = 1.25
product_name = "Bone Snack"
print(product_name)
print(price_per_unit)
print(quantity_of_pet_supplies)
print(
    "Child Name",
    product_name,
    "Timoula",
    price_per_unit,
    "Kasxia",
    quantity_of_pet_supplies,
)


def calculate_total_price(quantity: int, price_per_unit: float) -> float:
    total_price = quantity * price_per_unit
    return total_price


final_price = calculate_total_price(
    quantity=quantity_of_pet_supplies, price_per_unit=price_per_unit
)
print(final_price)

my_name = input("Please Type Your Name And Press Enter:")
print("Your Name Is", my_name)
