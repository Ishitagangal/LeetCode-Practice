'''
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
'''
class Solution:
    # recursive with memoization
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        operations = {
            '*' : lambda x, y: x * y,
            '-' : lambda x, y: x - y,
            '+' : lambda x, y: x + y
        }

        def calculate(expression, memo):
            result = []
            if expression in memo:
                return memo[expression]
            if expression.isdigit():
                return [int(expression)]

            for i, char in enumerate(expression):
                if char not in ('*', '-', '+'):
                    continue
                leftResult = calculate(expression[0:i], memo)
                rightResult = calculate(expression[i+1:], memo)

                for l in leftResult:
                    for r in rightResult:
                        result.append(operations[char](l, r))
            memo[expression] = result
            return result
        return calculate(expression, memo)