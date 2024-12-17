from functools import reduce

def _sum(arr):

    # iterate over array
    # using reduce and get
    # sum on accumulator
    sum = reduce(lambda a, b: a + b, arr)

    return sum


# driver function
arr = []
# input values to list
arr = [12, 3, 4, 15]

# calculating length of array
n = len(arr)

ans = _sum(arr)

# display sum
print("Sum of the array is ", ans)
