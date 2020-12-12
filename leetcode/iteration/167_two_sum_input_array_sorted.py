class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d = dict()
        for i, num in enumerate(numbers):
            d[num] = i

        for i, num in enumerate(numbers):
            remainder = target - num
            if remainder in d and d[remainder] > i:
                return [i + 1, d[remainder] + 1]
