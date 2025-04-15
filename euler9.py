# Euler 9
#
# a < b < c
# a² + b² = c²
# a + b + c = 1000 (there is only 1 value)
# find: a * b * c

# takes 38s to find on laptop (battery)
# now 0.03s! (removing one degree of freedom!)

from timer import timer
        
def do():
    for a in range(3, 1_000):
        for b in range(4, 1_000):
            #for c in range(3,1_000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2: #and a+b+c == 1_000:
                print(f"{a=} {b=} {c=}")
                return a*b*c

@timer()
def main() -> None:
    print(do())

if __name__ == "__main__":
    main()
