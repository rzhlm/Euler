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
    if not (len(n_str) % 2 == 0):
        return False
    if n < 2:
        return False
    length: int = len(n_str)
    half: int = length // 2
    a: int = int(n_str[: half])
    b: int = int(n_str[half:])
    if n_str[half:].startswith("0"):
        return False
    return (a + b)**2 == n

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
    print(list_2025_to_n)
    return list_2025_to_n


def T_func(n: int, start: int = 1) -> int:
    """Sum of all '2025-numbers', with n digits or less
    input: n ('n' digits in length, or less)
    output: sum (int)
     """
    all_2025: list[int] = create_2025(n, start)
    #print("T-func: sum:", sum(all_2025))
    return sum(all_2025)
    

def solve() -> None:
    # i=2 result=81 0.0000s
    # i=4 result=5131 0.0021s
    # i=6 result=499340 0.0330s
    # i=8 result=163868053 3.5621s
    for i in range(10, 17, 2):
        start = time.time()
        result: int = T_func(i, 10)
        stop = time.time()
        print(f"{i=} {result=} {stop-start:.4f}s")


def testing() -> None:
    assert is_2025(2025)
    assert is_2025(3025)
    assert is_2025(81)
    assert not is_2025(2026)
    assert not is_2025(9801)
    assert n_digits(4) == 9999
    assert T_func(4) == 5131


@timer()
def main() -> None:
    testing()
    solve()


if __name__ == "__main__":
    main()
