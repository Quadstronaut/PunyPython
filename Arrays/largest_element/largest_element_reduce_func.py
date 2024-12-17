# Python3 program to find maximum
# in arr[] of size n
from functools import reduce


def largest(arr):

    # Sort the array
    ans = reduce(max, arr)

    return ans
    # or returning largest value


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr)
print("Largest in given array ", Ans)
