# You will be given a list of 32 bit unsigned integers. Flip all the bits ( 1 -> 0 and 0 -> 1)
# and return the result as an unsigned integer.

# Example
#   n = 9_10
#   9_10 = 1001_2. We are working with 32 bits, so: 
#   00000000000000000000000000001001_2 = 9_10
#   11111111111111111111111111110110_2 = 4294967286_10
#   Return 4294967286.

# Function Description
#   Complete the fliiping Bits Function in the editor below:
#   flippingBits has the following parameter(s):
#       int n: an integer

# Returns 
#   int: the unsigned decimal integer result

# Input format
#   the first line of the input contains q, the bumber of queries. each of 
#   the next q lines contain an integer, n, to process.

# Constraints
#   1<= q <= 100
#   0<= n < 2^32

# Sample input
#   "3 
    # 2147483647 
    # 1 
    # 0"

# Sample Output
# "2147483648 
# 4294967294 
# 4294967295"

# Explanation

# Take 1 for example, as unsigned 32-bits is 00000000000000000000000000000001 and doing the flipping we get 11111111111111111111111111111110 which in turn is 4294967294.


def flippingBits(n):
    #res = ~n & 0xffffffff
    res = n ^ ((1 << 32) - 1)
    print(res)

flippingBits(1)