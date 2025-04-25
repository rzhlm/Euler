# Euler 940
#
# A(m,n)
# A(0,0) = 0
# A(0,1) = 1
# weird notation:
# A(m+1, n) = A(m, n+1) + A(m,n)
# A(m+1, n+1) = 2*A(m+1, n) + A(m,n)
#
# S= sum_{i=2}^k sum_{j=2}^k A(f_i, f_j)
# S(3) = A(1,1) + A(1,2) + A(2,1) + A(2,2)
# = 2+5+7+16
# = 30
# (note, according to defintion above, it should be A(2,2)+A(2,3)+A(3,2)+A(3,3))
# S(5) = 10_396
#
# Find S(50) and modulo it with 112_358_1313
# ############################################################################

from timer import timer


def A(m, n):
    print(f"entering A with {m=} {n=}")
    if m <= 0 and n <= 0:
        return 0
    elif m <= 0 and n == 1:
        return 1
    elif m == 1 and n == 1:
        return 2
    elif m == 1 and n == 2:
        return 5
    elif m == 2 and n == 1:
        return 7
    elif m == 2 and n == 2:
        return 16

    #A(m+1, n) = A(m, n+1) + A(m,n)
    # =A(m,n-1) = A(m-1, n) + A(m-1,n-1)
    # =A(m-1,n-2) = A(m-2,n-1) + A(m-2,n-2)
    # ? = A(m,n) = A(m-1,n+1) + A(m-1,n)
    #
    # A(m+1, n+1) = 2*A(m+1,n) + A(m,n)
    # =
    # A(m,n) = 2*A(m, n-1) + A(m-1, n-1)
    # A(m-1,n-1) = 2*A(m-1,n-2) + A(m-2, n-2)
    #
    # eg A(1,1) = A(0+1, 1) (m=0,n=1): A(0,2) + A(0,1)
    #  = + 1
    #---------------
    # A(m+1,n+1) = 2*A(m+1,n) + A(m,n)
    # A(m+1,n+1) - 2*A(m+1,n) = A(m,n)
    #
    # A(m+1,n) = A(m,n+1) + A(m,n)
    # A(m+1,n) - A(m,n+1) = A(m,n)
    #
    # A(m+1,n+1) - 2*A(m+1,n) = A(m+1,n) - A(m,n+1)
    # A(m+1, n+1) - 3*A(m+1,n) = -A(m, n+1)
    # A(m+1, n+1) = 3A(m+1,n) - A(m, n+1)
    # A(m,n) = 3A(m, n-1) - A(m-1, n)
    # 
    print(f"end of A, returning ")
    #return 
    #return 2*A(m, n-1) + A(m-1, n-1)
    # eq 1 inside eq 2:
    return 2*(A(m-1,n)+A(m-1,n-1)) + A(m-1, n-1)


def S(k):
    s = 0
    for i in range(1, k):
        for j in range(1, k):
            s += A(i, j)
    return s

def testing():
    assert A(1,1) == 2
    assert A(1,2) == 5
    assert A(2,1) == 7
    assert A(2,2) == 16
    
    assert S(3) == 30
    assert S(5) == 10_396


def main():
    testing()
    # find S(50) % 112_358_1313


main()
