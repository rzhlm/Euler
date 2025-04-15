# Euler 5
#
# smallest number (positive), evenly divisible by all the numbers from 1-20?
# (with no remainder)
# e.g. 2520 is smallest from the numbers from 1-10

# 1*2*3*4*5*6*7*8*9*10 = 10! = 3_628_800
# 20! = 2'432'902'008'176'640'000
# 

# check the Wikipedia article:
# One LCM algo: find the prime-factors for each value
# then find the maximum of that particular prime number, over all factors
# use these as exponents, and multiply


from timer import timer
from math import lcm

def prime_factors(num: int) -> list:
    factors = []
    f = 2
    while num > 1:
        if num % f == 0:
            factors.append(f)
            num = num // f
        else:
            f += 1
    return factors

def find_LCM(inputlist: list) -> int:
    x_dict = {}
    prime_dict = {}
    for n in inputlist:
        x_dict[n] = prime_factors(n)
    for vallist in x_dict.values():
        for val in vallist:
            if val not in prime_dict:
                prime_dict[val] = 1
            counts = vallist.count(val)
            maxcount = max(counts, prime_dict[val])
            prime_dict[val] = maxcount

# prime_dict {2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1}
# 
    output = 1
    for key, val in prime_dict.items():
        output *= key ** val
    #print(f"{output=}")
    return output

# {
# 2: [2],
# 3: [3],
# 4: [2, 2],
# 5: [5],
# 6: [2, 3],
# 7: [7],
# 8: [2, 2, 2],
# 9: [3, 3],
# 10: [2, 5],
# 11: [11],
# 12: [2, 2, 3],
# 13: [13],
# 14: [2, 7],
# 15: [3, 5],
# 16: [2, 2, 2, 2],
# 17: [17],
# 18: [2, 3, 3],
# 19: [19],
# 20: [2, 2, 5]
# }
#

def stdlib_LCM(inputs):
    return lcm(inputs)

@timer()
def main() -> None:
    #pass
    #print(find_divisors(100))
    #print(find_divisors(TESTNUM))
    #print(find_divisors(2520))
    #print(find_divisors(MAXNUM))
    #print(prime_factors(10))
    print(find_LCM(list(range(2, 20+1))))
    #print(stdlib_LCM(list(range(2, 21))))

if __name__ == "__main__":
    main()
