# Euler 3
#
# The prime factors of 13_195 are 5, 7, 13, 29
# What is the largest prime factor of the number 600_851_475_143

import functools
import math
import multiprocessing
import time

NUMBER = 600_851_475_143
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

# We will find all divisors of a number
# We will then keep only the divisors which are prime
# And then find the maximum value

""""
def find_divisors(num: int) -> list:
    start = time.time()
    divisors = []
    for i in range(2, num + 1):
        skip = False
        for prime in primes:
            if num % prime == 0:
                skip = True
                break
        if num % i == 0 and not skip:
            divisors.append(i)
            if True:
                split = time.time()
                duration = split - start
                pct = 100 * i / NUMBER
                print(f"finding divisors, now at {i=}")
                print(f"thus, we've done {pct}%")
                print(f"it has taken {duration} seconds")
                print(f"therefore, {100/pct*duration:.1f} is the total duration")
                print(f"or {100/pct*duration/3600:.1f} hours\n")
        elif skip:
            skip = False
            continue
            
    return divisors

   # return [
   #     i for i in range(2, num + 1) if num % i == 0
   # ]

def is_prime(num: int) -> bool:
    #print("inside is_prime: ", find_divisors(num))
    #print(f"{len(find_divisors(num))=}")
    #
    global primes
    
    if num in primes:
        return True
    
    if num != 2 and num % 2 == 0:
        return False
    elif num != 3 and num % 3 == 0:
        return False
    elif num != 5 and num % 5 == 0:
        return False
    elif num != 7 and num % 7 == 0:
        return False
    elif num != 11 and num % 11 == 0:
        return False
    
    if len(find_divisors(num)) == 1:
        primes.append(num)
        print("primes currently:", primes)
        return True

def keep_prime_divisors(divisors: list) -> list:
    return filter(is_prime, divisors)
"""


def factorize(num):
    start = time.time()
    factors = []
    f = 2

    while num > 1:
        if num % f == 0:
            factors.append(f)
            num = num // f
        else:
            f += 1
    stop = time.time()
    print(f"duration: {stop - start:.4f} seconds")
    return factors

def optimized_factorize(num):
    start = time.time()
    factors = []
    f = 2
    while f <= num ** 0.5:
        while num % f == 0:
            num = num // f
        f += 1
    if num > 1:
        factors.append(num)
    stop = time.time()
    duration = stop - start
    print(f"duration: {duration:.4f} seconds")
    return factors

@functools.cache
def main() -> None:
    #divisors = find_divisors(13_195)
    #primes = keep_prime_divisors(divisors) # should be 5, 7, 13, 29
    #print(max(list(primes))) # should be 29

    #divisors = find_divisors(NUMBER)
    #primes = keep_prime_divisors(divisors)
    #maxd = max(list(primes))
    #print(f"{maxd=}")

    print(factorize(13_195))
    print(factorize(NUMBER))
    print(optimized_factorize(NUMBER))

if __name__ == "__main__":
    main()
