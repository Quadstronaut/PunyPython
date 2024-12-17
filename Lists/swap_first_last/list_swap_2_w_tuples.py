# Swap function
def swapList(list):

    # Storing the first and last element
    # as a pair in a tuple variable get
    get = list[-1], list[0]

    # unpacking those elements
    list[0], list[-1] = get

    return list


# Driver code
newList = [4, 8, 15, 16, 23, 42]
print(swapList(newList))
