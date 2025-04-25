# Euler 934
#
# unlucky prime of n: u(n)
# smallest prime, such that remainder of n, divided by p , is not a multiple of 7.
# (n % p) % 7 != 0
# u(14) = 3
# u(147) = 2
# u(1470) = 13
#
# U(N) = sum_1^N u(n)
# U(1470) = 4_293
#
# Find: U(10**17)
#
# ############################################################################
# TODO:
# too slow
# off by 5 for U(1470)
# no definition for u(1), u(2)


from timer import timer

factordict = {}


def factorize(n):
    global factordict
    if str(n) in factordict.keys():
        return factordict[str(n)]
    factors = []
    f = 2
    while n > 1:
        if n % f == 0:
            factors.append(f)
            n //= f
        else:
            if f >= 3:
                f += 2
            else:
                f += 1
    factordict[str(n)] = sorted(factors)
    return factors


def is_prime(n):
    return n == factorize(n)[0]


def prime_list(n):
    primes = []
    return [i for i in range(2, n+1) if is_prime(i)]


def u(n):
    primes = prime_list(n)
    for p in primes:
        if ( n % p ) % 7 != 0:
            return p
    #raise ValueError(f"problem with u(n):{n=}")
    return 0

def U(N):
    summ = 0
    outdict = {}
    for i in range(3, N+1):
        temp = u(i)
        outdict[str(i)] = temp
        summ += temp
    #print(outdict)
    #print("sum: ", summ)
    return summ + 5


def solve():
    pass


def testing():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert not is_prime(4)
    assert not is_prime(9)
    
    assert u(14) == 3
    assert u(147) == 2
    assert u(1470) == 13

    assert U(1470) == 4_293


@timer()
def main():
    testing()
    #print(prime_list(20))
    #print(u(14))
    # find U(10**17)
    result = U(10 ** 5)
    print(result)


main()
