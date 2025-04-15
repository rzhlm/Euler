# Euler 9
#
# a < b < c
# a² + b² = c²
# a + b + c = 1000 (there is only 1 value)
# find: a * b * c

# takes 38s to find on laptop (battery)

from timer import timer

def do():
    a, b, c = 3, 4, 4
    while True:
        if a**2 + b**2 == c**2 and a + b +c == 1_000:
            print(f"triplet: {a=} {b=} {c=}")
        
def do2():
    for a in range(3, 1_000):
        for b in range(3,1_000):
            for c in range(3,1_000):
                if a**2 + b**2 == c**2 and a+b+c == 1_000:
                    print(f"{a=} {b=} {c=}")
                    return

@timer()
def main() -> None:
    do2()

if __name__ == "__main__":
    main()
