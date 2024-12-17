# Swap function
def swapList(list):
    
    start, *middle, end = list
    list = [end, *middle, start]
    
    return list
    
# Driver code
newList = [4, 8, 15, 16, 23, 42]

print(swapList(newList))