# Euler 26
#
# for 1/d, find the d (< 1_000), which has the longest recurring cycle
# e.g. 1/6 = 0.166666 (1 recurring)
# e.g. 1/7 = 0.142857_142857_142857, etc (6 digits)
#

from timer import timer

def is_divisible(n: int, d: int) -> bool:
    # to remove unuseful numbers like 1/9 etc
    return n % d == 0

def count_denom(n: int) -> int:
    frac = str(1 / n)
    frac = frac[1:]
    output: list[int] | None = []
    for i in range(2, 1_000):
        output.append((i, str(1/i)))
    return output

def solve() -> int:
    pass

def testing() -> None:
    pass

def main() -> None:
    result = count_denom(1)
    print(result)

if __name__ == "__main__":
    main()
