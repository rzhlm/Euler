# Euler 10
#
# The sum of the primes below 10 is 2+3+5+7 = 17
#  Find the sum of all the primes below two million.

from timer import timer

def era_sieve(num: int):
    # create a list of Bools, their index is the standin for the number
    # We're not explicitly going to check for prime, but just remove multiples
    prime_bools = [True] * (num + 1)
    prime_bools[0] = False
    prime_bools[1] = False

    for n in range(2, int(num**0.5)+1):
        if prime_bools[n] == True:
            for multiple in range(n*n, num + 1, n):
                prime_bools[multiple] = False
    primes = [id for id, boolean in enumerate(prime_bools) if boolean == True]
    return primes

@timer()
def main() -> None:
    assert sum(era_sieve(10)) == 17
    result = era_sieve(2_000_000)
    print("sum: ", sum(result))

if __name__ == "__main__":
    main()
