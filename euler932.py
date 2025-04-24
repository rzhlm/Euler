# Euler 932
#
# 2025 = (20 + 25)²
# a, b > 0 (integer)
# 3025 = (30 + 25)²
# 81 = (8+1)²
# We call this a "2025-number"
#
# T(n) = Sum of all these "2025-nums", with n or fewer digits
# T(4) = 5131
# find T(16)
#
# ############################################################################

from timer import timer
import time


def is_2025(n: int) -> bool:
    n_str : str = str(n)
    if n < 2:
        return False
    length: int = len(n_str)
    half: int = length // 2
    if len(n_str) % 2 == 0:
        a: int = int(n_str[: half])
        b: int = int(n_str[half:])
        if n_str[half:].startswith("0"):
            return False
        return (a + b) ** 2 == n
    elif length >= 2 and len(n_str) % 2 != 0:
        a: int = int(n_str[: half])
        b: int = int(n_str[half:])
        if n_str[half:].startswith("0"):
            return False
        return (a + b) ** 2 == n
    else:
        return False

def n_digits(n: int) -> int:
    """When given the input of 'n' requested digits, will make
    the appropriate limit
    """
    # eg. n_digits(4) -> from 1 to 9999
    # eg n_digits(3) -> from 1 to 999
    # eg n_digits(2) -> from 1 to 99
    # eg n_digits(1) -> from 1 to 9
    limit: int = int("9" * n)
    return limit


def create_2025(n: int, start: int = 1) -> list[int]:
    limit: int = n_digits(n)
    iter = range(start, limit + 1)
    list_2025_to_n: list[int] = list(filter(is_2025, iter))
    #print(list_2025_to_n)
    return list_2025_to_n

def create_2025bis(n: int, start: int = 1) -> list[int]:
    limit: int = n_digits(n)
    iter = range(start, limit + 1)

    half: int = n // 2
    #a_start: int = int("1" + (half - 1) * "0")
    a_start: int = 10 ** (half - 1)
    a_root_start: int = int(a_start ** 0.5) + 1
    #a_end: int = int("9" * half)
    a_end: int = 10 ** (half) - 1
    outlist = []
    for a in range(a_start, a_end + 1):
        for b in range(a_start, a_end + 1):
            if (a + b) < a_root_start:
                continue
            target = int(str(a) + str(b))
            if (a + b) ** 2 == target:
                outlist.append(target)
        
    return outlist


def create_2025tris(n: int, start: int = 1) -> list[int]:
    steps = n // 2
    local_solutions: list[int] = []
    for s in range(1, steps + 1):   
        half: int = s
        a_start: int = 10 ** (half - 1)
        a_end: int = 10 ** (half) - 1
        a_root_start: int = int(a_start ** 0.5) # + 1
        squares: list[int] = [i*i for i in range(a_root_start, a_end + 1)]
        all_2025 = list(filter(is_2025, squares))
        local_solutions += all_2025
    local_solutions = list(set(local_solutions))
    print(f"{n=} {local_solutions=}")
    return local_solutions
        
        
def T_func(n: int, start: int = 1) -> int:
    """Sum of all '2025-numbers', with n digits or less
    input: n ('n' digits in length, or less)
    output: sum (int)
     """
    all_2025: list[int] = create_2025tris(n, start)
    return sum(all_2025)
    

def solve() -> None:
    # NOT: 69245339400175715
    # NOT: 69245339399676375
    """
    for i in range(2, 16 + 1, 2):
        start = time.time()
        result: int = T_func(i, 1)
        stop = time.time()
        print(f"{i=} {result=} {stop-start:.4f}s")
    """
    result = T_func(16)
    print(f"final result: {result}")


def testing() -> None:
    assert is_2025(2025)
    assert is_2025(3025)
    assert is_2025(81)
    assert is_2025(74578140_11780496)
    assert is_2025(88_209)
    assert not is_2025(2026)
    assert not is_2025(9801)
    assert n_digits(4) == 9999
    assert T_func(4) == 5131
    assert create_2025(2) == [81]
    assert create_2025bis(2) == [81]
    assert create_2025tris(2) == [81]
    assert create_2025(4) == [81, 2025, 3025]
    assert create_2025tris(2) == [81]
    assert create_2025tris(4) == [81, 2025, 3025]
    assert create_2025tris(6) == [81, 2025, 3025, 88209, 494209]


@timer()
def main() -> None:
    testing()
    solve()


if __name__ == "__main__":
    main()
