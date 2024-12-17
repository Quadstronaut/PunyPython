# Swap function
def swapList(newList):
    size = len(newList)

    # Swapping
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList


# Driver code
srcList = [4, 8, 15, 16, 23, 42]
print("Original: ", srcList)
print("XSwapped: ", swapList(srcList))
