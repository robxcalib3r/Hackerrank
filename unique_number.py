# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
#   a = [1,2,3,4,3,2,1]
#    The unique element is 4.

# Function Description
#   Complete the lonelyinteger function in the editor below.

#   lonelyinteger has the following parameter(s):
#       int a[n]: an array of integers

# Returns
#   int: the element that occurs only once

# Input Format
#   The first line contains a single integer, , the number of integers in the array.
#    The second line contains  space-separated integers that describe the values in .

# Constraints
#   1<=n<100
#   It is guaranteed that  is an odd number and that there is one unique element.
#    0<=a[i]<=100, where 0<=i<n


def lonelyinteger(a):
    n = len(a)
    print(f'n: {n}')
    taken = [False] * n
    for i in range(n):
        print(f'i: {i}')
        if not taken[i]:
            taken[i] = True
            if i == n-1: return a[i]
            for j in range(i+1, n):
                if a[i] == a[j]:
                    taken[j] = True
                    print(f'a[{i}] == a[{j}]')
                    break
                elif a[i] != a[j] and j == n-1:
                    return a[i]

if __name__ == '__main__':
    a = [0,0,1,2,1]

    result = lonelyinteger(a)
    print(result)