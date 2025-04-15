# Euler 2
#
# By considering the terms in the Fibonacci sequence whose values
# do not exceed 4M, find the sum of the even-valued terms.

import functools

#limit = 4_000_000

@functools.cache
def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def make_list_of_evens(limit: int) -> list:
    num = 0
    i = 0
    output = []
    while num <= limit:
        i += 1
        num = fib(i)
        if num % 2 == 0:
            output.append(num)
    return output

def main() -> None:
    solution = sum(make_list_of_evens(4_000_000))
    print(solution)
    # edit: 4_613_732

if __name__ == "__main__":
    main()
