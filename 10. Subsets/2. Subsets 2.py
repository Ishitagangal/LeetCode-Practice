class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(index = 0, subset = []):
            result.append(list(subset))
            for i in range(index, len(nums)):
                if nums[i] == nums[i - 1] and index < i:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
                
        
        result = []
        backtrack()
        return result
