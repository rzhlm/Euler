# Euler 17
#
# If the numbers 1-5 are written out in words: one, two, three, four, five,
#  then there are 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive
#  were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example,
#  342 (three hundred and forty-two) contains 23 letters and
#  115 (one hundred and fifteen) contains 20 letters.
#  The use of "and" when writing out numbers is in compliance with British usage.
#

# CONSTANTS
numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def speak(n: int) -> str:
    if n == 1000:
        return "one thousand"
    elif 100 <= n < 1000:
        first = int(str(n)[0])
        second = int(str(n)[1]) * 10
        third = int(str(n)[2])
        if n % 100 == 0:
                return f"{numbers[first]} hundred"
        elif second < 20 and third != 0:
            return f"{numbers[first]} hundred and {numbers[int(str(n)[1:])]}"
        elif second < 20 and third == 0:
            #print(f"{first=} {second=} {third=} elif th=0")
            return f"{numbers[first]} hundred and {numbers[second]}"
        elif third == 0:
            return f"{numbers[first]} hundred and {numbers[second]}"
        else:
            #print(f"{first=} {second=} {third=} else th!=0")
            return f"{numbers[first]} hundred and {numbers[second]} {numbers[third]}"
    elif 20 < n < 100:
        first = int(str(n)[0]) * 10
        second = int(str(n)[1])
        if second == 0:
            return f"{numbers[first]}"
        else:
            return f"{numbers[first]} {numbers[second]}"
    else:
        return numbers[n]

def strlen(word: str) -> int:
    word = "".join(word.split(" "))
    return len(word)

def solve() -> None:
    cumul = 0
    for i in range(1, 1001):
        #print(speak(i))
        cumul += strlen(speak(i))
    print("Solution: ", cumul)

def main() -> None:
    result = speak(942)
    assert strlen(speak(342)) == 23
    assert strlen(speak(115)) == 20
    solve()
    #result = speak(115)
    #print(result)

if __name__ == "__main__":
    main()
