class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index = 0, subset = []):
            result.append(list(subset))
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        result = []
        backtrack()
        return result
    
    