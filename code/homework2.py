# write a function that uses looping to compute the first N Fibonacci numbers,
# where N is a parameter to the function.
# The Fibonacci sequence is defined as follows:

# The first two numbers in the sequence are 0 and 1
# The Nth number is the sum of the (N-1)th and (N-2)th numbers
# For example, if N is 10, the function should return the first 10 Fibonacci numbers:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

N = int(input("Enter the number of fibonnaci digits to print: "))

def compute_fibonacci(N):
    # do some work here that computes the first N Fibonacci numbers and prints them