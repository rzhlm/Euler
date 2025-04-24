# Euler 938
#
# card deck. R red, B blacks
# uniform random selection.
# 1 card selected and removed. Second card selected & removed
# then
# if both are red: discard
# if both are black: back into deck
# if different: red back, black discarded
#
# game ends when all remaning cards are same colour
#
# P(R,B) : prob that the remaining cards are black
# P(2,2) = 0.4666667 = 4/10 + 6/10/9 = 36/90 + 6/90 = 42/90
# P(10,9) = 0.4118903397
# P(34,25) = 0.3665688069
#
# ----> Find P(24_690, 12_345) (with 10 digits after decimal)
#
#
# ############################################################################

from timer import timer
import random


def select_card(R:int, B:int) -> int:
    selection = random.randint(1,2)
    if selection == 1:
        return "Red"
    elif selection == 2:
        return "Black"
    else:
        raise NotImplementedError()


def play(R: int, B: int):
    # R: initial red cards
    # B: initial black cards
    deck = []
    for _ in range(R):
        deck.append("R")
    for _ in range(B):
        deck.append("B")
    rounds = 0
    blackWon = None
    #print(f"start: {R=} {B=} {rounds=} {blackWon=}")
    while R != 0 and B != 0:
        rounds += 1
        #print(f"\titer-start: {R=} {B=} {rounds=} {blackWon=}")
        card1 = random.choice(deck)
        deck.remove(card1)
        card2 = random.choice(deck)
        deck.remove(card2)
        #print(f"\t{card1=} {card2=}")
        if card1 == "R" and card2 == "R":
            R -= 2
        elif card1 == "B" and card2 == "B":
            deck.append('B')
            deck.append('B')
            continue
        elif (card1 == "B" and card2 == "R") or (card1 == "R" and card2 == "B"):
            B -= 1
            deck.append('R')
        else:
            raise NotImplementedError()
    if R > 0 and not B > 0:
        blackWon = False
    elif B > 0 and not R > 0:
        blackWon = True
    else:
        raise NotImplementedError()
    #print(f"end: {R=} {B=} {rounds=} {blackWon=}")
    #print("-"*10)
    #return {'blackWon': blackWon, 'red': R, 'black': B, 'rounds':rounds,}
    return blackWon

def solve(R:int, B:int, runs: int):
    print(f"{R=} {B=} {runs=}")
    totals = []
    for _ in range(runs):
        #blackWon, _, _, _ = play(2, 2)
        blackWon = play(R, B)
        totals.append(blackWon)
        #print("blackWon: ", blackWon)
        #print("totalslist ", totals)
        #print("solve: ", result)
    print(f"{sum(totals)=} / {runs=} = {sum(totals)/runs}:.4f")
    freq_prob = sum(totals)/runs
    return freq_prob

def testing() -> None:
    assert round(solve(2, 2, 100_000),2) == 0.47

@timer()
def main() -> None:
    testing()
    solve(2, 2, 1_000_000)
    solve(10, 9, 100_000)
    solve(34, 25, 100_000)
    print("\n\n")
    solve(24_690, 12_345, 100)
    


if __name__ == "__main__":
    main()
