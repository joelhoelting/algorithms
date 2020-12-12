"""
169. Majority Element
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1

        for num in nums:
            if num == majority:
                count += 1
            else:
                count -= 1
                if count == 0:
                    majority = num
                    count = 1

        return majority


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = list(set(nums))
        print(arr)

        for num in arr:
            if nums.count(num) > int(len(nums) // 2):
                return num
