# Euler 12
#
# which number (which is triangular), is the first with >500 divisors?
# 
# triangular(n): adding up naturals including n
# 7th triangular = 28
# factors: factors of 28: 1,2,4,7,14,28 (6 factors)

from timer import timer
import functools
from itertools import count

def triangular(n: int) -> int:
    return sum([i for i in range(1, n+1)])

@functools.cache
def rec_triangular(n: int) -> int:
    if n == 1:
        return 1
    return n + rec_triangular(n-1)

# should be slow, but is faster than the other solution
# but still way too slow
def find_factors(num: int) -> list:
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors

def faster_factors(num: int) -> list:
    # start by dividing instead of checking each value first
    factors = []
    f = 2    
    while num > 1:
        if num % f == 0:
            factors.append(f)
            num //= f
        else:
            f += 1
    return factors

# other way: find prime factors, and then multiples of those
def prime_factors(num: int) -> list:
    primes = [True] * (num + 1)
    primes[0] = primes[1] = False

    for n in range(2, int(num**0.5)+1):
        if primes[n]:
            for multi in range(n*n, num +1, n):
                primes[multi] = False

    prime_factors = [n for n in range(2, num+1) if primes[n] and num%n == 0]
    #primelist = [id for id, boolean in enumerate(primes) if boolean]
    #return primelist
    return prime_factors

# with a Boolean list, for memory & speed
def other_factors(num: int, primes: list) -> list:
    multiples = [False] * (num + 1)
    multiples[1] = True

    #prime_factors = [prime for prime in primes if num % prime == 0]

    for n in range(2, num+1):
        if num % n == 0:
            for prime in primes:
                if n % prime == 0:
                    multiples[n] = True
                    break

    multilist = [id for id, boolean in enumerate(multiples) if boolean]
    return multilist

def other_fac_check(num, primes):
    ## using a value list instead of a boolean list, hunting down a bug
    factors = []
    for n in range(1, num + 1):
        if num % n == 0:
            temp = n
            for prime in primes:
                while temp % prime == 0:
                    temp = temp // prime
            if temp == 1:
                factors.append(n)
    return factors
    
def go(num=0):
    assert rec_triangular(7) == 28
    assert len(find_factors(28)) == 6

    infinite_iter = count(start=2080)

    for i in infinite_iter:
        t = triangular(i)
        f = find_factors(t)
        #f = faster_factors(t)
        l = len(f)
        if l > 350:
            print(f"{i=} {t=} {l=}")
            return

# This is 4 times slower than the find_factors above:
def go_num(n, logg=False):
    #t = rec_triangular(n)
    p = prime_factors(n)
    o = other_factors(n, p)
    if logg:
        print(f"input {n=} has become triangular {n=}")
        print(f"and t has prime factors: {p=}")
        print(f"and t has all factors: {o}")
    return o



@timer()
def main() -> None:
    go(1_000)

if __name__ == "__main__":
    main()
