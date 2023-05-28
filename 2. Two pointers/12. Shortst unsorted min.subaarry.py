class Solution:
    def findUnsortedSubarray2(self, nums):
        if len(nums) <2:
            return 0
        
        prev = nums[0]
        end = 0
		# find the largest index not in place
        for i in range(0, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        start = len(nums) - 1
        prev = nums[start]
		# find the smallest index not in place
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]
        if end != 0:
            return end - start + 1
        else: 
            return 0
    #[2,6,4,8,10,9,15]
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # find inflection points, start and end for window size
        end = 0
        start = len(nums) - 1
        max_val = nums[0] # largest value i've seen so far
        min_val = nums[len(nums) - 1]
        for i in range(len(nums)):
            if max_val <= nums[i]: 
                max_val = nums[i]
            else:
                end = i 
                 # if we come across a value smaller than nums[0] which was largest we saw, out of order needs to be sorted
        
        for i in range(len(nums)-1, -1, -1):
            if min_val >= nums[i]:
                min_val = nums[i]
            else:
                start = i
        if end!=0 : return end - start + 1
        return 0
