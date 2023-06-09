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
    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:    
        result = []
        def backtrack(remaining_target, combo, start):
            if remaining_target == 0:
                result.append(combo[:])
                return
            
            elif remaining_target < 0:
                return
            
            for i in range(start, len(candidates)):
                combo.append(candidates[i])
                backtrack(remaining_target - (candidates[i]), combo, i)
                combo.pop()
        
        backtrack(target, [], 0)
        return result