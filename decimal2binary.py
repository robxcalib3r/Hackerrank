# Decimal to Binary Conversion 

# Steps
#   1. Divide the given decimal number by 2 where it gives the result along with the remainder
#   2. if the given decimal number is even, then the result will be whole and it gives the remainer 0
#   3. if the given decimal number is odd, then the result is not divided properly and it gives the remainder 1
#   4. By placing all the remainders in order in such a way, the least significant bit (LSB) at the top and MOst Significant bit (MSB)
#       at the bottom, the required binary number will be otained.


def dec2bin(num):
    base = 1
    bin = 0
    div = num // 2
    remain = num % 2
    while True:
        bin = base * remain + bin
        base *= 10
        print(bin)
        if div == 0: break
        remain = div % 2
        div = div // 2
        print(f'div: {div}, remain: {remain}')


def dec2bin_eff(num):
    strs = ""
    while num:
        if (num & 1):
            strs += "1"
        else:
            strs += "0"
        
        num >>= 1

    if strs == "":
        print("0")
    else:
        print(strs[::-1])


dec2bin_eff(2)