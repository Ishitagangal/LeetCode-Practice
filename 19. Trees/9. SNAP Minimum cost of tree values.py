class Solution:
    # use stack likenext greater eleemnt
    def mctFromLeafValues(self, arr: List[int]) -> int:
        result = 0
        stack = [float(inf)]
        for num in arr:
            while stack[-1] <= num:
                min_element = stack.pop()
                result += min_element * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            result += stack.pop() * stack[-1]
        return result

    def mctFromLeafValues2(self, A): # O(n^2)
#       We remove the element form the smallest to bigger.
#       We check the min(left, right),
#       For each element a, cost = min(left, right) * a
        res = 0
        while len(A) > 1:
            i = A.index(min(A))
            res += min(A[i - 1:i] + A[i + 1:i + 2]) * A.pop(i)
        return res