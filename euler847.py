# Euler 847
#
# a integer N is distributed over 3 locations. We're looking for 1 item out of these N
# we can make subsets and ask questions whether the subset includes the item
#
# h(a,b,c) = minimum questions required to have certainty
# h(1,2,3) = 3
# h(2,3,3) = 4
# 
# H(N): sum of h(a,b,c); a,b,c non-negative Integer,
# and 1 <= a+b+c <= N
# H(6) = 204
# H(20) = 7_717
# H(111) = 1_634_144
# 
# Rn (repunit) : n digits of 1: e.g; R3 = 111
#
# -> find H(R19), then mod 1_000_000_007 for answer

def h(a: int,b: int,c: int) -> int:
    # h(1,2,3) = 3
    # h(2,3,3) = 4
    pass

def H(N: int) -> int:
    # H(6) = 204
    # H(20) = 7_717
    # H(111) = 1_634_144
    pass

def R(n: int) -> int:
    return int("1"*n)


def test():
    assert R(3) == 111
    
    # assert h(1,2,3) == 3
    # assert h(2,3,3) == 4
    # 
    # assert H(6) == 204
    # assert H(20) == 7_717
    # assert H(R(3)) == 1_634_144

def main() -> None:
    test()

if __name__ == "__main__":
    main()
