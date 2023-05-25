class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first_num = 1, curr = []):
            if len(curr) == k:
                result.append(curr[:])
            
            for i in range(first_num, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        
        result = []
        backtrack()
        return result