# Euler 938
#
# ############################################################################
#
# (semi-)analytical attempt
# edit:
# calculate asymptotic probability
# 1st attemped recursion, but limit is too low for succes
# then attempted to build a value-table and use that instead


from timer import timer
from functools import cache
import sys


@cache
def rec_iterate(R, B):
    if R <= 0 and B > 0:
        return 1
    elif B <= 0 and R > 0:
        return 0
    
    # if probs = None:
    #    probs = {'pRR': 0, 'pRB': 0, 'pBR': 0, 'pBB': 0 }
    
    # RR: prob for R = R - 2
    pRR = (R / (R + B)) * ((R - 1)/(R + B - 1))
    # follow from basic probability, and from combinations:
    # R_C_2 / (R+B)_C_2
    """
    if R % 2 != 0:
        minRR = (R + 1) // 2
    else:
        minRR = R // 2
    """
    
    # RB: prob for B = B - 1
    pRB = (R / (R + B)) * (B / (R + B - 1))
    # how many RB's needed at minimum?
    # B = B

    # BR: prob for B = B - 1
    pBR = (B / (R + B)) * (R / (R + B - 1))

    # BB: prob for B = B
    pBB = (B / (R + B)) * ((B - 1) / (R + B - 1))
    # this one has no impact

    # P(R,B) = pRR*P(R-2,B) + pRB*P(R, B-1) + pBB*P(R,B)
    # P(R,B) - pBB*P(R,B) = pRR*P(R-2,B) + pRB*P(R, B-1)
    # P(R,B) (1 - pBB) = ...
    # P(R,B) = [pRR*P(R-2,B) + pRB*P(R, B-1)] / (1-pBB)

    # p(RB / ^BB) = pRB / (1-pBB) = 2B / ((R - 1) + 2B)
    # p(RR / ^BB) =  ... = (R - 1) / ((R-1) + 2B)
    #
    p_asympt_RB = 2 * B / ((R - 1) + 2 * B)
    p_asympt_RR = (R - 1) / ((R - 1) + 2 * B)
    
    # P(0,B) = 1 # Black wins
    # P(A,0) = 0 # Black loses

    #P(R,B) =
    p = p_asympt_RR * rec_iterate(R-2,B) + p_asympt_RB * rec_iterate(R, B-1)
    return p
    

def testing() -> None:
    assert rec_iterate(2, 2) == 7/15
    assert rec_iterate(10, 9) == 0.41189033965989136
    assert rec_iterate(34, 25) == 0.36656880694764005


def make_table(R,B):
    table = [[None for _ in range(B+1)] for _ in range(R + 1)]

    for b in range(B+1):
        table[0][b] = 1
    for r in range(2, R+1, 2):
        table[r][0] = 0

    for r in range(2, R + 1, 2):
        for b in range(1, B+1):
            table[r][b] = ((r-1)/((r-1)+2*b)) * table[r-2][b] \
                + ((2*b)/((r-1)+2*b)) * table[r][b-1]

    return table

@timer()
def main():
    #print(sys.getrecursionlimit()) # = 1000
    #sys.setrecursionlimit(40_000)
    testing()
    R = 24_690
    B = 12_345
    #R = B = 2
    #result = rec_iterate(R, B)
    table = make_table(R,B)
    #print(table[2][2])
    result = table[R][B]
    print(result)
    #print(f"{R=} {B=} {result=}")


main()
