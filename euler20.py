# Euler 20
#
# 100! factorial
# find sum of digits
#

from timer import timer
from math import factorial


def solve():
    num = factorial(100)
    num_str = str(num)
    num_split = list(num_str)
    summ = sum(map(int, num_split))
    return summ

def main() -> None:
    print(solve())

if __name__ == "__main__":
    main()
