class Solution:
    def largestRectangleArea(self, heights:List[int]) ->int:
        if not heights or len(heights) == 0:
            return 0
        n = len(heights)
        smaller_on_left = [-1] * n # store index of first bar on the left smaller than i
        smaller_on_right = [-1] * n # store index of first bar on the right smaller than i
        smaller_on_left[0] = -1
        smaller_on_right[n-1] = len(heights)

        for i in range(1, n):
            p = i - 1
            while p>=0 and heights[p] >= heights[i]:
                p = smaller_on_left[p] # jump to index calculated by i-1th index since if i-1 is greater than i it may have already found index of element smaller than it(i-1th)
            smaller_on_left[i] = p
        
        for i in range(n-2, -1, -1):
            p = i + 1
            while p < n and heights[p] >= heights[i]:
                p = smaller_on_right[p]
            smaller_on_right[i] = p
        max_area = 0
        # max area for bar of height i is its height * width between smallest bars on either side
        for i in range(n):
            max_area = max(max_area, heights[i] * (smaller_on_right[i] - smaller_on_left[i] - 1))
        return max_area


    #monotonic stack solutions
    def largestRectangleAreaStack(self, heights: List[int]) -> int:
        stack, max_area = [], 0
        for i, height in enumerate(heights + [0]):
            while stack and height <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else (i - stack[-1] - 1)
                max_area = max(max_area, h*w)
            stack.append(i)
        return max_area