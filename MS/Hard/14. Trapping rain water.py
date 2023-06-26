class Solution:
    # https://leetcode.com/problems/trapping-rain-water/solutions/1374608/c-java-python-maxleft-maxright-so-far-with-picture-o-1-space-clean-concise/
    # for ith index find maximum bar before it and after it. use that to calculate
    # water level above ith index possible
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left, max_right = [0]*n, [0]*n

        for i in range(1, n):
            max_left[i] = max(height[i-1], max_left[i-1])
        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i+1], max_right[i+1])
        
        result = 0
        for i in range(n):
            water_level = min(max_left[i], max_right[i])
            if water_level >=height[i]:
                result += water_level - height[i]
        return result        