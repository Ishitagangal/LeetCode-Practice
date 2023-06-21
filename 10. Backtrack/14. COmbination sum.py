class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtrack(target, combo, next_num):
            if target == 0 and len(combo) == k:
                result.append(combo[:])
                return
            
            for i in range(next_num, 9):
                combo.append(i+1)
                backtrack(target - i - 1, combo, i+1)
                combo.pop()
        
        backtrack(n, [], 0)
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