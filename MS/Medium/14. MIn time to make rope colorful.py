# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.
class Solution:
    # 1 pointer
    def minCost(self, colors:str, neededTime:List[int]) -> int:
        total_time = 0
        curr_max = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                curr_max = 0
            total_time += min(curr_max, neededTime[i])
            curr_max = max(curr_max, neededTime[i])
        return total_time

    # 2 pointers, 
    def minCost2pointer(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        left, right = 0, 0
        while left <len(neededTime) and right <len(neededTime):
            curr_total = 0
            curr_max = 0
            while right < len(neededTime) and colors[left] == colors[right]:
                curr_total += neededTime[right]
                curr_max = max(curr_max, neededTime[right])
                right += 1
            total_time += curr_total - curr_max # keep the max val, remove the others
            left = right
        return total_time