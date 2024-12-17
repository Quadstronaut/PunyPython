# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
    for i in range(gcd(d, n)):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


# UTILITY FUNCTIONS
# function to print an array


def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")


# Function to get gcd of a and b


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]

# Calls function to rotate_by value, and of_size value
leftRotate(arr, 2, 7)
printArray(arr, len(arr))
