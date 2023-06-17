class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start = 0):
            if start == len(nums):
                result.append(list(nums))
            
            visited = set()
            for i in range(start, len(nums)):
                if nums[i] not in visited:
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]
                    visited.add(nums[i])
        result = []
        backtrack()
        return result