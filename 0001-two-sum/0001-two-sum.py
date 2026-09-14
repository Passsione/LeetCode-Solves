class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 2:
            return [0, 1]
        
        for i in range(size):
            for j in range(size - 1, i, -1):
                if nums[i] +  nums[j] == target and (j != i):
                    return [i, j]
