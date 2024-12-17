def swap_first_last_3(lst):
    # Check if list has at least 2 elements
    if len(lst) >= 2:
        # Swap the first and last elements using slicing
        lst = lst[-1:] + lst[1:-1] + lst[:1]
    return lst


# Initializing the input
inp = [4, 8, 15, 16, 23, 42]

# Printing the original input
print("The original input is:", inp)

result = swap_first_last_3(inp)

# Printing the result
print("The output after swap first and last is:", result)
