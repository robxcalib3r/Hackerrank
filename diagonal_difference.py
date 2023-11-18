# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix 'arr' is shown below:
#       1 2 3
#       4 5 6
#       9 8 9

# The left-to-right diagonal = 1+5+9 = 15
# The right-to-left diagonal = 3+5+9 = 17
# Their absolute difference is = | 15-17 | = 2

## Function description
#   digaonalDifference takes the following parameterr:
#       - int arr[n][m] : an array of integers

## Return
#   - the absolute diagonal difference

## Input format
#   the first line contains a single integer, n, the number of rows and columns in the square
#       matrix 'arr'
#   Each of the next n lines describes a row, arr[i], and consists of n space-separated integers arr[i][j]

## Constraints
#   -100 <= arr[i][j] <= 100

## Output format
#   return the absolute difference between the sums of the matrix's two diagonals as a single integer

## Sample Input
#   " 3
#     11 2 4
#     4 5 6
#     10 8 -12"

# # Sample Output
#       "15"


def diagonalDifference(arr):
    dia1 = dia2 = 0
    rev = 2
    for i in range(0,3):
        dia1 += arr[i][i]
        dia2 += arr[i][rev]
        rev -= 1
    
    return abs(dia1 - dia2)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)