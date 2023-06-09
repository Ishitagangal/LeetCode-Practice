class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while(left < right):
            minimum_height= min(height[left], height[right]) # limit to be able to hold water
            max_area = max(max_area, minimum_height * (right - left))
            if(height[left] < height[right]):
                left+=1
            else:
                right-=1
        return max_area