# Euler 10
#
# The sum of the primes below 10 is 2+3+5+7 = 17
#  Find the sum of all the primes below two million.

from timer import timer

primes = []
factor_dict = {}

def factorize(num: int) -> list:
    global factor_dict
    orig_num = num
    factors = []
    if num in factor_dict:
        return factor_dict[num]
    
    f = 2
    while num > 1:
        if num % f == 0:
            factors.append(f)
            num = num // f
        else:
            if f >= 3:
                f += 2
            else:
                f += 1
    #print("factorisation done")
    factor_dict[orig_num] = factors
    return factors

def is_prime(num: int) -> bool:
    if num in primes:
        return True
    if num == factorize(num)[0]:
        primes.append(num)
        return True
    else:
        return False

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

def find_primes_below(num:int) -> list:
    global primes
    #primes = []
    for i in range(2, num + 1):
        if i% (num//100) == 0:
            print(f"{i} out of {num} = {100*i/num}%")
        if is_prime(i):
            continue

@timer()
def main() -> None:
    assert sum(era_sieve(10)) == 17
    print(factorize(20))
    #find_primes_below(2_000_000)
    result = era_sieve(2_000_000)
    print(result)
    print("sum: ", sum(result))
    #print(primes)
    #print("sum: ", sum(primes))

if __name__ == "__main__":
    main()
