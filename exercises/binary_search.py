class Solution:
    def search(self, nums: list[int], target: int) -> int:
        (start, end) = (0, len(nums) - 1)

        while start <= end:
            middle = start + (end - start) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
        
        return -1