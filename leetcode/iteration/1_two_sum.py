"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


# def two_sums(nums, target):
#     curr_idx = 0

#     while curr_idx < len(nums) - 1:
#         curr_num = nums[curr_idx]
#         rest_of_arr = nums[curr_idx + 1:len(nums)]
#         for i in range(len(rest_of_arr)):
#             if curr_num + rest_of_arr[i] == target:
#                 print([curr_idx, curr_idx + (i+1)])
#                 return [curr_idx, curr_idx + (i+1)]

#         curr_idx += 1


# two_sums([12, 10, 2, 3, 4], 15)

# def two_sums_two_pass(nums, target):
#     d = {}
#     for i, n in enumerate(nums):
#         d[n] = i

#     for i, n in enumerate(nums):
#         remainder = target - n
#         print(i, n)
#         if remainder in d and i != d[remainder]:
#             print([i, d[remainder]])
#             return [i, d[remainder]]


# two_sums_two_pass([3, 2, 4], 6)


def two_sums_one_pass(nums, target):
    d = {}
    for i, n in enumerate(nums):
        remainder = target - n
        if remainder in d:
            return [d[remainder], i]
        else:
            d[n] = i

    return []


two_sums_one_pass([3, 2, 4], 6)
