my_name = input(
    "Hello! Welcome to our online shop G.T.A. Trading LTD. Please input your name to continue.\n"
)
print("Hello", my_name)
my_surname = input("Please input your surname.\n")
print(my_name, my_surname, "welcome to G.T.A. Trading LTD")
product_name = "Bone Snack 150gr"
product_price = 1.50
unit_quantity = 6
print(product_name, product_price, "x", unit_quantity)


def calculate_total_price(quantity: int, price_per_unit: float) -> float:
    total_price = quantity * price_per_unit
    return total_price


final_price = calculate_total_price(
    quantity=unit_quantity, price_per_unit=product_price
)
print("Your total is", final_price)
print("Thank you for your purchase!")
