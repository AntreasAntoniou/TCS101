# Given a number N,
# which denotes the number of prime numbers
# I want to generate, in ascending order,
# starting from 1, generate all first N prime numbers
from typing import List, Callable


def check_if_number_is_prime_naive(number: int, previous_prime_numbers: List[int]):
    is_prime = True  # start with the assumption that the number IS prime
    for i in range(2, number):  # iterate from 2 to current number
        if (
            number % i == 0
        ):  # check if current number is visible perfectly by i and if it is
            is_prime = False  # this is not a prime number
            break  # exit the for loop
    return is_prime


def check_if_number_is_prime_efficient(number: int, previous_prime_numbers: List[int]):
    is_prime = True  # start with the assumption that the number IS prime
    for i in previous_prime_numbers:  # iterate from 2 to current number
        if (
            number % i == 0
        ):  # check if current number is visible perfectly by i and if it is
            is_prime = False  # this is not a prime number
            break  # exit the for loop
    return is_prime


# 2, 3, 5, 7
# N = 10, please check if prime
# if N is not divisible by previous primes (2, 3, 5, 7) then it will necessarily be a prime itself,
# and this is because, the other numbers can already be divided by those primes


def compute_first_N_prime_numbers(N: int, is_prime_function: Callable):
    prime_number_list = []  # start from empty list
    current_number = 2  # number 0 and 1 are not prime, so start from 2

    while (
        len(prime_number_list) < N
    ):  # keep looping until you have N items in you prime number list
        is_prime = is_prime_function(
            current_number, prime_number_list
        )  # check if current number is prime
        if is_prime is True:  # if prime is True
            prime_number_list.append(current_number)  # add number to our prime list
        current_number = current_number + 1  # go to the next number to check

    return prime_number_list


import time

N = int(input("Please enter an N, so we can generate the first N prime numbers\n"))
start_time = time.time()
prime_numbers_naive = compute_first_N_prime_numbers(N, check_if_number_is_prime_naive)
end_time = time.time()
time_elapsed_naive = end_time - start_time
# print("The first N prime numbers are:", prime_numbers_naive)
print("This took", time_elapsed_naive, "seconds")
start_time = time.time()
prime_numbers_efficient = compute_first_N_prime_numbers(
    N, check_if_number_is_prime_efficient
)
end_time = time.time()
time_elapsed_efficient = end_time - start_time
# print("The first N prime numbers are:", prime_numbers_efficient)
print("This took", time_elapsed_efficient, "seconds")
print("Speed up ratio", time_elapsed_naive / time_elapsed_efficient)
