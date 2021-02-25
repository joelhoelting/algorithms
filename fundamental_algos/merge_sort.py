# Recursion and Divide & Conquer

# Runtime: 
# Best Case: O(n log n)
# Worst Case: O(n^2)

def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[half:])
    right = merge_sort(array[:half])
    print(left, right)

    return merge(left, right)

print(merge_sort([17,87,6,22,41,3,13,54]))