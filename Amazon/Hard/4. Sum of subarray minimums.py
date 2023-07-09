class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr # to avoi dempty stack
        result = [0] * len(arr)
        stack = [0]
        for i in range(len(arr)):
            while stack and arr[i]< arr[stack[-1]]:
                stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i-j) * arr[i]
            stack.append(i)
        return sum(result) %(10**9+7)