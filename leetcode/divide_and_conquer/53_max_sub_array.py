"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-2147483647]
Output: -2147483647
"""


def max_crossing_subarray(a, low, mid, high):
    left_sum = -float("inf")
    current_sum = 0
    print(a, low, mid, high)
    for i in range(mid, low - 1, -1):
        print(i)
        current_sum += a[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i
    right_sum = -float("inf")
    current_sum = 0
    for j in range(mid + 1, high + 1):
        current_sum += a[j]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)


def max_subarray(a, low, high):
    if low == high:  # base case
        return (low, high, a[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = max_subarray(a, low, mid)
        right_low, right_high, right_sum = max_subarray(a, mid + 1, high)
        cross_low, cross_high, cross_sum = max_crossing_subarray(
            a, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)


if __name__ == '__main__':
    change = [1, 3, -2, 6]
    m = max_subarray(change, 0, len(change) - 1)
    # print("change =", change)
    # print("maximum subarray:")
    # print("start:", m[0], " end:", m[1], " maximum sum:", m[2])
