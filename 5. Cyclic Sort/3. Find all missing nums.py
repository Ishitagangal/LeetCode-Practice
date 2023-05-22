class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # cyclic sort idea, without sorting. mark index where it should be
        # two passes

        for i in range(len(nums)):
            valid_position = abs(nums[i]) - 1 # nums 1 to n+1. n should be at n-1 index
            if nums[valid_position] > 0:
                nums[valid_position] *= -1 # mark i as visited
        
        result = []
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                result.append(i)
        
        return result