class Solution:
# Input: arr = [2,1,3,4,4]
# maxof left = [2,2,3,4,4]
# minofright = [1,1,3,4,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
# For a increasing straight line , (Max at i) < (Min of I + 1)...
# i.e [1..4] max =4 , [5..7] min in 5 ,
# So , If Max < Min , then there is no element on the right side , who belongs on the left side as per above observation.
# if Max > Min, it means , there is some element on the right side, who belongs on the left, so we CANNOT create a chunk.
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 1

        max_on_left = [-math.inf] * n
        min_on_right = [math.inf] * (n)

        max_on_left[0] = arr[0]
        min_on_right[-1] = arr[-1]
        result = 1
        for i in range(1, n):
            max_on_left[i] = max(max_on_left[i-1], arr[i])
            min_on_right[n-i-1] = min(min_on_right[n-i], arr[n-i-1])
        
        for i in range(n-1):
            if max_on_left[i] <= min_on_right[i+1]:
                result +=1
        return result