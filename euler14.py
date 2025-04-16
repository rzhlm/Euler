# Euler 14
#
# Collatz sequence
# which number (< 1M) produces the longest chain?
#
# ca 30s execution time on laptop (battery)

from timer import timer


def go_odd(n: int) -> int:
    return 3*n + 1

def go_even(n: int) -> int:
    return n // 2

def is_even(n: int) -> bool:
    if n & 1 == 0:
        return True
    return False

def go_collatz(n: int) -> int:
    if is_even(n):
        return go_even(n)
    else:
        return go_odd(n)
    
def go_len(n: int) -> int:
    i = 0
    while n != 1:
        i += 1
        #print(f"{i=} {n=}")
        n = go_collatz(n)
    if n == 1:
        i += 1
    return i

def save_lengths(n:int) -> (int, int):
    #lengths = []
    #len_dict = {}
    maxkey = 0
    maxlen = 0
    
    for i in range(1, n):
        length = go_len(i)
        #len_dict[i] = length
        if length > maxlen:
            maxlen = length
            maxkey = i
    #print(len_dict)
    return (maxkey, maxlen)

@timer()        
def main() -> None:
    assert 10 == go_len(13)
    result = save_lengths(1_000_000)
    print(result)

if __name__ == "__main__":
    main()
