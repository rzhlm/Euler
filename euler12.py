# Euler 12
#
# which number (which is triangular), is the first with >500 divisors?
# 
# triangular(n): adding up naturals including n
# 7th triangular = 28
# factors: factors of 28: 1,2,4,7,14,28 (6 factors)

# 5.8s on laptop (battery), not using recursion
# 10 runs: 7.6-7.7s
# 2.8s on laptop (battery), with recursion
# 10 runs recusion: 3.9-4.0s
# functional: 12-14s! surprising, I expected it to be faster

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

def functional_triangular(n: int) -> int:
    result = functools.reduce(lambda x,y: x+y, range(1,n+1))
    return result

# should be slow, but is faster than the other solution
# but still way too slow
def find_factors(num: int) -> list:
    factors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            factors.append(i)
            factors.append(num//i)
    return factors

def go():
    assert rec_triangular(7) == 28
    assert len(find_factors(28)) == 6

    #infinite_iter = count(start=2080)
    infinite_iter = count(start = 1)

    for i in infinite_iter:
        #t = rec_triangular(i)
        t = functional_triangular(i)
        f = find_factors(t)
        l = len(f)
        if l > 500:
            print(f"{i=} {t=} {l=}")
            return

@timer()
def main() -> None:
    go()

if __name__ == "__main__":
    main()
