# Euler 7
#
# find the 10_001st prime num
# eg 2,3,5,7 (7th is 4th prime num)
#

# comes in at 62 seconds on my laptop, running on battery.
# Should be <60s according to the rules
# edit: after adding a 2-digit step in prime_factors: 36s
# edit: counting instead of making a list makes no difference (count_primes)
# edit: functools.cache neither

from timer import timer
import functools

@functools.cache
def prime_factors(num: int) -> list:
    """factorizes a number into a list of its prime factors"""
    factors = []
    f = 2
    while num > 1:
        if num % f == 0:
            factors.append(f)
            num = num // f
        else:
            if f >= 3:
                f += 2
            else:
                f += 1
    return factors

@functools.cache
def is_prime(n):
    return n == prime_factors(n)[0]

def find_primes(limit = 10):
    """returns a list of sequential primes, until the limit-th prime"""
    primes = [2, 3]
    i = 5
    while len(primes) < limit:
        if is_prime(i):
            primes.append(i)
            #print("new prime: ", i)
        i += 2
    return primes

@functools.cache
def count_primes(limit = 10):
    """returns the limit-th prime"""
    primes = [2, 3]
    counter = 2
    i = 5
    while counter < limit:
        if is_prime(i):
            counter += 1
            #print("new prime: ", i)
        i += 2
    return i-2
    

def do():
    #print(prime_factors(10))
    #print(prime_factors(11))
    assert is_prime(10) == False
    assert is_prime(11) == True

@timer()
def main() -> None:
    #do()
    #print(find_primes(4)[-1])
    answer = count_primes(10_001)
    print(answer)

if __name__ == "__main__":
    main()
