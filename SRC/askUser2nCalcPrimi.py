import time
from math import isqrt

def is_prime(number, time_stats=False):
    """
    Determines if a number is prime.
    
    Args:
        number (int): The number to check.
        time_stats (bool): Whether to measure execution time (optional).

    Returns:
        list: [is_prime (bool), first_multiplier (int)], where:
            - is_prime: True if number is prime, False otherwise.
            - first_multiplier: The first divisor found if number is not prime, 0 otherwise.
    """
    if number < 2:
        return [False, 0]  # Numbers less than 2 are not prime

    is_prime = True
    first_multiplier = 0
    start_time = time.process_time() if time_stats else None

    for i in range(2, isqrt(number) + 1):  # Loop up to the square root of the number
        if number % i == 0:
            is_prime = False
            first_multiplier = i
            break

    if time_stats:
        elapsed_time = time.process_time() - start_time
        print(f"Execution time: {elapsed_time:.5f} seconds")

    return [is_prime, first_multiplier]

# User input and execution
user_number = int(input("Choose a number and press enter: "))
answer = is_prime(user_number, time_stats=True)

if answer[0]:
    print(f"{user_number} is prime!")
else: 
    print(f"{user_number} is not prime, the first multiplier found is {answer[1]}")
