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
    
def go(num: int):
    assert rec_triangular(7) == 28
    assert len(find_factors(28)) == 6

    infinite_iter = count(start=7)

    for i in infinite_iter:
        t = triangular(i)
        f = find_factors(t)
        l = len(f)
        if l > 100:
            print(f"{i=} {t=} {l=}")
            return

def go_num(n, logg=False):
    #t = rec_triangular(n)
    p = prime_factors(n)
    o = other_factors(n, p)
    if logg:
        print(f"input {n=} has become triangular {n=}")
        print(f"and t has prime factors: {p=}")
        print(f"and t has all factors: {o}")
    return o

@timer(10)
def bench_t():
    sum = 0
    for i in range(1, 1000):
        sum += triangular(i)

@timer(10)
def bench_rec():
    sum = 0
    for i in range(1, 1000):
        sum += rec_triangular(i)


def test_primes():
    f = prime_factors(20)
    print(f)


def solve():
    for i in range(1, 1_000):
        t = rec_triangular(i)
        factors = go_num(t)
        if len(factors) > 500:
            print("FOUND: ",t)
            return

@timer()
def main() -> None:
    #go_until(10)
    #print(go_num(10))
    #print(other_fac_check(10, [2, 5]))
    #print(other_factors(10, [2,5]))
    #print(triangular(1_000))
    #bench_t()
    #bench_rec()
    #go()
    #test_primes()
    #solve() # 40s
    go(1_000)

if __name__ == "__main__":
    main()
