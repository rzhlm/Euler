# Euler 25
#
# index of Fibonacci term which is first with 1_000 digits
#

##############################################################################
# imports
#
from timer import timer
from functools import cache, reduce
from itertools import count

##############################################################################
# functions
#
@cache
def rec_fibonacci(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return rec_fibonacci(n - 1) + rec_fibonacci(n - 2)

# def tail_fibonacci()
#    
def solve() -> int:
    iter = count(1)
    for i in iter:
        result: int = rec_fibonacci(i)
        if len(str(result)) == 1_000:
            return i

##############################################################################
# testing
#
def testing() -> None:
    assert rec_fibonacci(3) == 2
    assert rec_fibonacci(10) == 55

##############################################################################
# consolidation
#
@timer()
def main() -> None:
    testing()
    result: int = solve()
    print(result)

if __name__ == "__main__":
    main()
