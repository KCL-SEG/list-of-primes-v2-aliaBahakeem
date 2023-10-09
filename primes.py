"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    return list
    def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Input must be a positive integer")
    
    prime_list = []
    num = 2  # Start with the first prime number
    
    while len(prime_list) < number_of_primes:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    
    return prime_list

# Test cases
try:
    result1 = primes(10)
    print(result1)  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]