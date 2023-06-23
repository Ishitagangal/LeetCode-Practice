class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(left, right, combo):
            if len(combo) == 2 * n:
                result.append(combo)
                # print(result)
                return
            
            if left < n:
                backtrack(left+1, right, combo + '(')
            
            if right < left:
                backtrack(left, right+1, combo + ')')
            
        backtrack(0, 0, '')
        return result


        