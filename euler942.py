# Euler 942
#
# q in N
# q-th Mersenne: p = 2^q - 1 (prime)
# R(q): (minimal sqrt of q) % p (if exists)
# = smallest int x such that x² - q is divisble by p
# smallest int such that x² - q % p == 0
#
# R(5) = 6
# R(17) = 47_569
#
# find R(74_207_281) % ((10 ** 9) + 7)
# ############################################################################

from timer import timer
from itertools import count

def give_mersenne() -> list[int]:
    """return the numbers 'n' where prime = (2 ** n) - 1 """
    return [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203,
         2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497,
          86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221,
           3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457,
            32582657, 37156667, 42643801, 43112609, 57885161, 74207281, 77232917,
             82589933, 136279841]

def give_squares(start:int, n: int) -> list[int]:
    # returns list of squares, up to n**2
    return [i*i for i in range(start, n + 1)]


def R(q: int) -> int:
    # smallest int x such that (x² -q) % p == 0
    # q: index of mersenne number: 1st, 2nd, etc
    p = (2 ** q) - 1
    if q == 74_207_281:
        sqrt = 8600 #p ** 0.5
    else:
        sqrt = p ** 0.5
    """
    for x in count(start=int(sqrt)-1, step=1):
        if (x*x - q) % p == 0:
            print("x found: ", x)
            return x
        #if x % 1_000 == 0:
        #    print("val")
    """
    squares = give_squares(1_000_000_000, 10_000_000_000)
    sq_set = set(squares)
    #start = int(round((p+q)**0.5,0))-1
    start = 1
    """
    for k in range(start, 100_000_000):
        if k*p + q in squares:
            print("FOUND!!",k)
            print("sqrt of: ", (k*p + q))
            print("which is:", int(round((k*p+q)**0.5,0)))
            x2 = (k*p + q)
            root = x2 ** 0.5
            sol = int(root)
            #print(f"{x2=} {root=} {sol=}")
            #print(type(sol))
            #return int(round(((k*p+q) ** 0.5),0))
            return sol
    """
    for sq in squares:
        if (sq - q) % p == 0:
            print("FOUND (square):", sq)
            print("root: ", sq**0.5)
            sol = int(round(sq**0.5,0))
            return sol
    print("#"*70)
    print("exhausted all the squares!")
    print("last square:", squares[-1])

        
def old_solve():
    output = []
    for mers in give_mersenne():
        output.append(R(q))
    return output


def solve():
    result = R(74_207_281)
    print("SOLVE RESULT :",result)
    return result



def testing() -> None:
    #assert R(5) == 6 # (6² - 5) % ((2**5)-1) == 0
    # or: 36-5 % 31 == 0:
    # or 31 % 31 == 0
    #assert R(17) == 47_569
    # (47569² - 17) % (2**17 -1) == 0
    pass
    
@timer()
def main() -> None:
    testing()
    result = solve()
    print(result)


if __name__ == "__main__":
    main()
