# Euler 24
#
# lexicographic permutation: ordered & sorted permutations
# what is 1M-th lexicographic perm of 0-9?
#

##############################################################################
# imports
#
from timer import timer
from itertools import permutations

##############################################################################
# functions
#
def make_perms(digits: list[int], length: int) -> list[tuple[int, int]]:
    output = permutations(digits, length)
    return list(output)

def solve() -> int:
    digits = list(range(10))
    result = make_perms(digits, len(digits))
    solution =  result[1_000_000 - 1]
    print(solution)
    sol_str = "".join(str(d) for d in solution)
    return int(sol_str)
##############################################################################
# testing
def testing() -> None:
    assert make_perms(list(range(3)), 3) == [(0, 1, 2), (0, 2, 1),
        (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]

##############################################################################
# consolidation
# 

@timer()
def main() -> None:
    testing()
    result = solve()
    print(result)

if __name__ == "__main__":
    main()
