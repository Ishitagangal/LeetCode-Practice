class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort array
        i = 0
        while i < len(nums):
            temp = nums[i]
            if temp < len(nums) and temp != i:
                nums[i], nums[temp] = nums[temp], nums[i]
            else:
                i+=1
        
        # find missing num
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)