# Euler 16
#
# sum of digits of
# 2**1000

def solve():
    num = 2**1000
    
    str_num = str(num)
    str_split = list(str_num)
    #print(str_split)
    
    summ = sum(map(int, str_split))
    print(summ)


def main() -> None:
    solve()

if __name__ == "__main__":
    main()
