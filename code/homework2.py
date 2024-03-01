# write a function that uses looping to compute the first N Fibonacci numbers,
# where N is a parameter to the function.
# The Fibonacci sequence is defined as follows:

# The first two numbers in the sequence are 0 and 1
# The Nth number is the sum of the (N-1)th and (N-2)th numbers
# For example, if N is 10, the function should return the first 10 Fibonacci numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

N = int(input("Enter the number of digits to print: "))

# bag_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print("The 5th number in the bag is", bag_of_numbers[4])


def print_first_N_numbers(N):
    bag_of_numbers = []
    for i in range(N):
        print(i)
        print(bag_of_numbers)
        bag_of_numbers.append(i)

    print(bag_of_numbers)
    sum_of_last_two_numbers = bag_of_numbers[N - 1] + bag_of_numbers[N - 2]
    print("The sum of the last two numbers is", sum_of_last_two_numbers)


print_first_N_numbers(N)


def compute_fibonacci(N):
    pass  # remove this line and replace it with your code
    # do some work here that computes the first N Fibonacci numbers and prints them


compute_fibonacci(N)
