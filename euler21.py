# Euler 21
#
# d(n) = sum of proper divisors of n
# if d(a) = b
# and d(b) = a (and a != b)
# then a,b is 'amicable pair', 'amicable nymbers'
#
# find sum of all amicable numbers < 10_000

##############################################################################
# imports

from timer import timer

##############################################################################
# functions 

def find_factors(n: int) -> list[int]:
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i) if i != 1 else None
    return factors

def sum_factors(n: int) -> int:
    return sum(find_factors(n))

def is_amicable(a: int) -> bool:
    x = sum_factors(a)
    y = sum_factors(x)
    if a == x:
        return False
    return a == y
        
def find_amicables(n: int) -> list[int]:
    amicables = []
    for i in range(n):
        if is_amicable(i):
            amicables.append(i)
    return amicables

##############################################################################
# testing part

def test_find_factors() -> None:
    assert sorted(find_factors(10)) == [1, 2, 5]
    assert sum_factors(10) == 8
    assert sum_factors(220) == 284
    assert sum_factors(284) == 220
    assert is_amicable(220)
    assert is_amicable(284)

def test():
    test_find_factors()

##############################################################################
# consolidation part:
#
@timer()
def main() -> None:
    test()
    r = find_amicables(10_000)
    print(sum(r))

if __name__ == "__main__":
    main()
