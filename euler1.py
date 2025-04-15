# Euler 1

def multiple_of_x(num: int, factor: int) -> bool:
    return num % factor == 0

def list_multiples_below(below: int, multiples_list: list) -> list:
    outlist = []
    for i in range(1, below):
        for m in multiples_list:
            if multiple_of_x(num=i, factor=m) and (i not in outlist):
                outlist.append(i)
    return outlist

def functional_list_multiples_below(below:int, multiples_list) -> list:
    return [
        n for n in range(1, below)
        if any(n % m == 0 for m in multiples_list)
    ]

def main() -> None:
    #pass
    #print(list_multiples_below(10, [3, 5])) # should be 23
    #print(sum(functional_list_multiples_below(10, [3, 5]))) # should be 23
    print(sum(functional_list_multiples_below(1000, [3, 5])))
    # edit: result is 233168
   
if __name__ == "__main__":
    main()

