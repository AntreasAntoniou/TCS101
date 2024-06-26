# This is my first comment

# Python has many types of data. Here are a few examples:

# Strings

# Strings are a sequence of characters. They are enclosed in single or double quotes.

# Examples:

name = "John"
surname = "Doe"
middle_name = "Quincy"

# Let's print them out:

# on a single line
print(name, middle_name, surname)

# on separate lines
print(name)
print(middle_name)
print(surname)

# Numbers

# Numbers can be integers or floats. Integers are whole numbers, while floats are numbers with decimal points.

# Examples:

age = 25
height = 1.75
weight = 65.5

# Let's print them out:

# on a single line
print(age, height, weight)

# on separate lines
print(age)
print(height)
print(weight)

# With descriptive strings in front of them:

# on a single line

print("age:", age, "height:", height, "weight:", weight)

# on separate lines

print("age:", age)
print("height:", height)
print("weight:", weight)

# Python math operations

# You can perform math operations in Python. Here are a few examples:

# Addition

# Examples:

addition = 1 + 2
print("addition:", addition)

# Subtraction

# Examples:

subtraction = 2 - 1
print("subtraction:", subtraction)

# Multiplication

# Examples:

multiplication = 2 * 3
print("multiplication:", multiplication)

# Division

# Examples:

division = 4 / 2
print("division:", division)

bmi = 85 / 1.86**2
print(bmi)


def compute_bmi(weight: float, height: float) -> float:
    square_height = height**2
    bmi = weight / square_height
    return bmi


# Let's print the result of the function:

my_age = 32
my_height = 1.86
my_weight = 88.5
my_bmi = compute_bmi(weight=my_weight, height=my_height)

print("my bmi:", compute_bmi(weight=my_weight, height=my_height))


def cook_spagetti_carbonara(cooked_spagetti, carbonara_sauce, hot_pan):
    pass


def cook_pasta(uncooked_pasta):
    pass


def make_carbonara_source(pancetta, parmegianno_regianno, cheese_2):
    pass


def heat_pan(pan):
    pass


carbonara_portion = cook_spagetti_carbonara(
    cooked_spagetti=cook_pasta(uncooked_pasta=None),
    carbonara_sauce=make_carbonara_source(pancetta=None),
    hot_pan=heat_pan(pan=None),
)

# Booleans

# Booleans are either True or False. They are used to represent the truth value of an expression.

# Examples:

is_raining = True
is_sunny = False

# Let's print them out:

# on a single line

print("is_raining:", is_raining, "is_sunny:", is_sunny)

# Using boolean operators

# with bigger and smaller than operators
my_age = 32

younger_than_18 = my_age < 18
equal_to_18 = my_age == 18
not_equal_to_18 = my_age != 18

older_than_18 = my_age > 18
older_than_or_equal_to_18 = my_age >= 18

print(
    f"older_than_18: {older_than_18}, younger_than_18: {younger_than_18}, equal_to_18: {equal_to_18}, not_equal_to_18: {not_equal_to_18}, older_than_or_equal_to_18: {older_than_or_equal_to_18}"
)
# using with if statements


if my_age > 18:
    print("I'm older than 18")
else:
    print("I'm younger than 18")

# using with elif statements

if my_age > 18:
    print("I'm older than 18")
elif my_age < 18:
    print("I'm younger than 18")
else:
    print("I'm 18")


# Homework

# Write a function that takes in a persons age and weight and returns their BMI along with a message that tells them if they are overweight, underweight or normal weight.

# BMI = weight / height**2

# BMI Categories:

# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater
