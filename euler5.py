# Euler 5
#
# smallest number (positive), evenly divisible by all the numbers from 1-20?
# (with no remainder)
# e.g. 2520 is smallest from the numbers from 1-10

# 1*2*3*4*5*6*7*8*9*10 = 10! = 3_628_800
# 20! = 2'432'902'008'176'640'000
# 
# lower bound: primes below 20:
# 19 * 17 * 13 * 11 * 7 * 5 * 3 * 2
# = 9_699_690

from timer import timer
from math import factorial

MAXNUM = factorial(20)
TESTNUM = factorial(10)
KNOWN_DIV = list(range(1,21))

def find_divisors(num: int) -> list:
    divisors = []
    for i in range(1, num+1):
        if i not in KNOWN_DIV:
            continue
        if num % i == 0:
            divisors.append(i)
    return divisors


def GCM():
    # find prime factorization
    # for each common prime factor, take the minimum value
    # multiply all
    pass

def LCM(num1, num2):
    # abs(num1, num2) / gcd(num1, num2)
    #
    pass

def prime_factors(num):
    factors = []
    f = 2
    while num > 1:
        if num % f == 0:
            factors.append(f)
            num = num // f
        else:
            f += 1
    return factors



@timer()
def main() -> None:
    #pass
    #print(find_divisors(100))
    #print(find_divisors(TESTNUM))
    #print(find_divisors(2520))
    #print(find_divisors(MAXNUM))
    print(prime_factors(10))

if __name__ == "__main__":
    main()
