class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash: dict[int, int] = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff], i]
            hash[num] = i
        
        return []
