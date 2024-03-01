# Looping

# There are several ways to loop in Python. The most common ones are:

# for loop: where you execute the same part of the code a fixed number of times


for i in range(0, 3):
    condition = input("Is the condition True? (Yes/No)\n")

    if condition == "Yes":
        print("The condition is True")
        break
    elif condition == "yes":
        print("The condition is True")
        break
    elif condition == "y":
        print("The condition is True")
        break
    elif condition == "Y":
        print("The condition is True")
        break
    elif condition == "No":
        print("The condition is False")
        break
    elif condition == "no":
        print("The condition is False")
        break
    elif condition == "n":
        print("The condition is False")
        break
    elif condition == "N":
        print("The condition is False")
        break
    else:
        print("Invalid input")


# while loop: where you execute the same part of the code as long as a condition is True
your_condition = input("Is the condition True? (Yes/No)\n")
while your_condition != "Yes":
    print("The condition is False")
    your_condition = input("Is the condition True? (Yes/No)\n")
