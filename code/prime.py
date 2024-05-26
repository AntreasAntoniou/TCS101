N = int(
    input(
        "Welcome to the prime number fact checker. Please input the X prime number you want to be computed:"
    )
)


def check_if_number_is_prime_prime(N: int):
    if N <= 1:
        return False
    for i in range(2, N):
        if N % i == 0:
            return False
    return True


def compute_prime_number(N: int):
    count = 0
    candidate = 2
    while True:
        if check_if_number_is_prime(candidate):
            count += 1
            if count == N:
                return candidate
        candidate += 1


print("The", N, "nth prime number is", compute_prime_number)

# Compute the Nth prime number
# Remember that i%5 will return the remainder when I is divided by 5
# /
