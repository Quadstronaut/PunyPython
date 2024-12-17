def sum_of_array(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_sum = sum_of_array(arr, low, mid)
    right_sum = sum_of_array(arr, mid + 1, high)
    return left_sum + right_sum


# Examples
arr = [1, 2, 3]
print(sum_of_array(arr, 0, len(arr) - 1))  # Output: 6

arr = [15, 12, 13, 10]
print(sum_of_array(arr, 0, len(arr) - 1))  # Output: 50
