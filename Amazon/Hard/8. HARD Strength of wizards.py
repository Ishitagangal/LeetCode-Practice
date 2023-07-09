class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        # next smaller on left and right
        # compute prefix sum and sum of prefix sums to find sum of prefix sums within an  index range quickly
        mod = 10 **9 + 7
        n = len(strength)
        right = [n] *n
        stack = []
        # next smaller on right of index i
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                right[stack.pop()] = i
            stack.append(i)
        
        # next smaller on left of index i, traverse right to left to find this
        left = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                left[stack.pop()] = i
            stack.append(i)
        
        prefix = [0]
        for num in strength:
            prefix.append(prefix[-1] + num)
        prefix_sums = [0] * len(prefix)
        for i in range(1, len(prefix)):
            prefix_sums[i] = prefix_sums[i-1] + prefix[i]
        # prefix_sums = list(accumulate(accumulate(strength), initial = 0))
        result = 0
        for i in range(n):
            l, r = left[i], right[i]
            prefix_left = prefix_sums[i] - prefix_sums[max(l, 0)]
            prefix_right = prefix_sums[r] - prefix_sums[i]
            result += (strength[i] * (prefix_right * (i-l) - prefix_left * (r-i))) % mod
        return result % mod