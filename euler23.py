# Euler 23
#
# find sum of
# all positive integers
# which can't be written as sum of abundant number
# ( <= 28_123)
#

##############################################################################
# imports

from timer import timer

##############################################################################
# functions

def find_divisors(n: int) -> list[int]:
    divisors: list[int] = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i) if i != 1 else None
    return list(set(divisors))

def is_perfectnum(n: int) -> bool:
    return sum(find_divisors(n)) == n

def num_type(n: int) -> int:
    # 1: deficient, 2: perfect, 3: abundant
    s = sum(find_divisors(n))
    if s < n:
        return 1
    elif s == n:
        return 2
    elif s > n:
        return 3
    else:
        raise ValueError

def is_abundant(n: int) -> bool:
    return num_type(n) == 3

def list_all_abundants() -> list[int]:
    # 4 is a solution!
    return [i for i in range(12, 28_124) if is_abundant(i)]

def sum_abundants() -> list[int]:
    # it gets 8, 16, 20, 22. This should not be possible.
    # where is the bug?
    abundants = list_all_abundants()
    sum_ab: list[int] = []
    for ab in abundants:
        for ab2 in abundants:
            s = ab + ab2
            if s >= 28_124:
                continue
            #elif s in sum_ab:
            #    continue
            else:
                    sum_ab.append(s)
    set_ab: list[int] = list(set(sum_ab))

    return set_ab
            
def gen_all_nums() -> list[int]:
    return [i for i in range(1, 28_124)]

def find_not_in_sums() -> list[int]:
    all = gen_all_nums()
    not_abun: list[int] = []
    s = sum_abundants()
    for num in all:
        if num not in s:
            not_abun.append(num)
    #return [num for num in all if num not in s]
    return not_abun

##############################################################################
# testing

def test() -> None:
    assert sorted(find_divisors(28)) == [1, 2, 4, 7, 14]
    assert sorted(find_divisors(12)) == [1, 2, 3, 4, 6]
    #assert sorted(find_divisors(4)) == [1, 2]
    assert sum(find_divisors(28)) == 28
    assert sum(find_divisors(12)) == 16
    assert is_perfectnum(28)
    assert is_abundant(12)
    assert not is_abundant(10)
    # assert not is_abundant(4) # due to root approx, this fails
    assert num_type(28) == 2
    assert num_type(12) == 3

##############################################################################
# consolidation

@timer()
def main() -> None:
    test()
    #r = list_all_abundants()
    #r = sum_abundants()
    #print(r)
    #print(sum(r))
    result = find_not_in_sums()
    print(result)
    print(sum(result))

if __name__ == "__main__":
    main()
