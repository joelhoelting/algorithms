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


def maxSubArray(nums):
    # Kadane's Algorithm
    # if len(nums) == 1:
    #     return nums[0]
    #
    max_curr = nums[0]
    max_glob = nums[0]
    for i in range(1, len(nums)):
        max_curr = max(max_curr + nums[i], nums[i])
        if max_curr > max_glob:
            max_glob = max_curr

    return max_glob


maxSubArray([-3, 5, 2, -3, 1, -2])
max_curr = 5, 7, 4, 5, 3
max_glob = 5, 7, 7, 7, 7
