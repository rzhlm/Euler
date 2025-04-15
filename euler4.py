# Euler 4
# 
# Find the largest palindrome from the product of two 3-digit nums
# eg abc * def = xy_dyx
# eg abc * def = xyd_dyx
#
# 100 * 100 = 10_000
# 999 * 999 = 998_001
#

#import time
from timer import timer

def is_palin(num: int) -> bool:
    return str(num) == str(num)[::-1]

def multiply_3x3() -> list:
    #start = time.time()
    results = []
    for x in range(100, 1000):
        for y in range(100, 1000):
            product = x * y
            if is_palin(product):
                results.append(product)
                #print(f"{x=} {y=} {x*y=}")
    #end = time.time()
    #print(f"duration: {end - start:.4f} seconds")
    return results

#@timer(iterations=30)
@timer()
def main() -> None:
    #print(is_palin(1001))
    #pass
    print(max(multiply_3x3()))

if __name__ == "__main__":
    main()
