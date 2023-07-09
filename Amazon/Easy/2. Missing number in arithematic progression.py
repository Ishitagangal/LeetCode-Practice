class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        difference = (arr[-1] - arr[0]) // n
        left, right = 0, n

        while left < right:
            mid  = left + (right - left)//2
            if arr[mid] == arr[0] + mid *difference:
                left = mid + 1
            else:
                right = mid
        return arr[0] + difference * right