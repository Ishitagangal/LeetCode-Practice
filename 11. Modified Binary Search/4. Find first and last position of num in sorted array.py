class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.findBound(nums, target, True)
        if start == -1:
            return [-1, -1]
        end = self.findBound(nums, target, False)

        return [start, end]
    
    def findBound(self, nums, target, isLowerBound):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] == target:
                # lower
                if isLowerBound:
                    if mid == low or nums[mid -1] < target:
                        return mid
                    high = mid - 1
                else: # upper
                    if mid == high or nums[mid+1]> target:
                        return mid
                    low = mid + 1

            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1