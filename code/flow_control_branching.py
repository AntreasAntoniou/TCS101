# with bigger and smaller than operators
# my_age = 32
# older_than_18 = my_age > 18
# younger_than_18 = my_age < 18
# equal_to_18 = my_age == 18
# not_equal_to_18 = my_age != 18
# older_than_or_equal_to_18 = my_age >= 18

# print(
#     f"older_than_18: {older_than_18}, younger_than_18: {younger_than_18}, equal_to_18: {equal_to_18}, not_equal_to_18: {not_equal_to_18}, older_than_or_equal_to_18: {older_than_or_equal_to_18}"
# )

# Flow control

# There are several ways to control the flow of your program. The most common ones are:

# Branching: where you execute different parts of the code depending on the value of some variables
# Looping: where you execute the same part of the code multiple times

# Branching

condition = input("Is the condition True? (Yes/No)\n")

if condition == "Yes":
    print("The condition is True")
elif condition == "yes":
    print("The condition is True")
elif condition == "y":
    print("The condition is True")
elif condition == "Y":
    print("The condition is True")
elif condition == "No":
    print("The condition is False")
elif condition == "no":
    print("The condition is False")
elif condition == "n":
    print("The condition is False")
elif condition == "N":
    print("The condition is False")
else:
    print("Invalid input")


your_age = int(input("What's your age?\n"))

if your_age > 21:
    print("You may enter the casino")
elif your_age == 21:
    print("You may enter the casino")
elif your_age < 5:
    print("Piene gorase pampers")
elif your_age < 21:
    print("You may not enter the casino")
else:
    print("Invalid input, please enter a number, and press enter")


bigger_than_18 = your_age > 18
smaller_than_18 = your_age < 18
bigger_or_equal_to_18 = your_age >= 18
smaller_or_equal_to_18 = your_age <= 18
equal_to_18 = your_age == 18
not_equal_to_18 = your_age != 18
