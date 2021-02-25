def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_set = set(nums)
    print(nums_set)

    for i in range(0, len(nums) + 1):
        if not i in nums_set:
            return i

def missingNumber(self, nums: List[int]) -> int:
    s = 0
    n = 1
    for i in nums:
        s ^= i
        s ^= n
        n += 1
    return s

