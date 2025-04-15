# Euler 6
#
# Find the difference between
# the sum of the squares
# of the first one hundred natural numbers
# and the square of their sum.
#

from timer import timer

def sum_first_n(n: int) -> int:
    # n * (n+1) / 2
    return n * (n + 1) // 2

def sum_of_squares(n: int) -> int:
    output = 0
    for i in range(1, n + 1):
        output += i ** 2
    return output

@timer()
def main() -> None:
    assert 5050 == sum_first_n(100)
    square_of_sum = sum_first_n(100) ** 2
    sum_squares = sum_of_squares(100)
    diff = abs(sum_squares - square_of_sum)
    print(diff)

if __name__ == "__main__":
    main()
