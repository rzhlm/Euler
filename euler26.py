# Euler 26
#
# for 1/d, find the d (< 1_000), which has the longest recurring cycle
# e.g. 1/6 = 0.166666 (1 recurring)
# e.g. 1/7 = 0.142857_142857_142857, etc (6 digits)
#
# -> we'll take as a starting point 6 digits and up
# python has 17 digits for floats
# arbitrary precision can be had with decimals.Decimal(n)
##############################################################################

from timer import timer
import decimal


def is_divisible(n: int, d: int) -> bool:
    # to remove unuseful numbers like 1/9 etc
    return n % d == 0


def count_denom(n: int) -> int:
    frac: str = str(round(1e6 / n, 17))
    # frac = frac[2:]
    # print(f"{frac=}")
    # output: list[int] | None = []
    # 1/1000 max, thus 0.001
    # Thus, we can expect to be able to check for 6 digits, and have to move
    # a bit, and that the recurring doesn't occur immediately

    size: int = 6
    # idx: int = 0
    count: int = 0
    for i in range(17 - size + 1):
        digit_part: str = frac[i: i + size]
        # print(f"{digit_part=}")
        count = frac.count(digit_part)
        # print(f"{count=}")
        if count > 1:
            return (count, digit_part)
        else:
            continue
    return (0, 0)

    # for i in range(2, 1_000):
    #    output.append((i, str(1/i)))
    # return output


def solve() -> int:
    for i in range(1, 1_000):
        c, val = count_denom(i)
        if c > 1:
            print(f"{i=} {c=} {val=}")


def testing() -> None:
    pass


def main() -> None:
    result = count_denom(7)
    print(result)
    result2 = solve()
    print(result2)


if __name__ == "__main__":
    main()
