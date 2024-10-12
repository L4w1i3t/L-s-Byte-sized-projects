"""
I asked ChatGPT to give me a REALLY suboptimal way to make a "Hello World" program. This is the result.
"""
import sys
import time
import threading
import multiprocessing
from functools import reduce
import random
import math

# Unnecessary global variables
GLOBAL_CONSTANT = 42
LARGE_PRIME = 15485863

def compute_pi(n_terms):
    """Compute Pi using the Leibniz formula (extremely inefficient for large n_terms)."""
    pi_over_4 = 0.0
    for k in range(n_terms):
        pi_over_4 += ((-1)**k) / (2*k + 1)
    return pi_over_4 * 4

def fibonacci(n):
    """Compute the nth Fibonacci number recursively (inefficient)."""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prime(n):
    """Check if a number is prime (inefficient for large n)."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_large_list(size):
    """Generate a large list of random numbers."""
    return [random.randint(1, 100) for _ in range(size)]

def sort_large_list(large_list):
    """Sort a large list using bubble sort (inefficient)."""
    n = len(large_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if large_list[j] > large_list[j + 1]:
                large_list[j], large_list[j + 1] = large_list[j + 1], large_list[j]
    return large_list

def unnecessary_threading():
    """Create unnecessary threads."""
    def worker():
        time.sleep(1)
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

def worker():
    """Worker function for multiprocessing."""
    time.sleep(1)

def unnecessary_multiprocessing():
    """Create unnecessary processes."""
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=worker)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

def calculate_factorial(n):
    """Calculate factorial using reduce (inefficient for large n)."""
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

def main():
    # Perform unnecessary computations
    pi = compute_pi(1000000)
    fib_number = fibonacci(30)
    prime_check = is_prime(LARGE_PRIME)
    large_list = generate_large_list(1000)
    sorted_list = sort_large_list(large_list)
    unnecessary_threading()
    unnecessary_multiprocessing()
    factorial_result = calculate_factorial(1000)

    # Build "Hello, World!" character by character using corrected ASCII codes
    chars = [
        chr(int(math.sqrt(5184))),             # 'H' (sqrt(5184) = 72)
        chr(int(math.ceil(math.e * 37))),      # 'e' (ceil(e * 37) = 101)
        chr(int(2 ** 7 - 20)),                 # 'l' (128 - 20 = 108)
        chr(int(2 ** 7 - 20)),                 # 'l'
        chr(int(math.sqrt(12321))),            # 'o' (sqrt(12321) = 111)
        chr(int(2 ** 5)),                      # ' ' (2^5 = 32)
        chr(int(174 / 2)),                     # 'W' (174 / 2 = 87)
        chr(int(math.sqrt(12321))),            # 'o'
        chr(int(3 * 38)),                      # 'r' (3 * 38 = 114)
        chr(int(2 ** 7 - 20)),                 # 'l'
        chr(int(10 ** 2 / 1))                  # 'd' (100 / 1 = 100)
    ]
    message = ''.join(chars)

    # Print the message
    sys.stdout.write(message + '\n')

if __name__ == "__main__":
    main()
