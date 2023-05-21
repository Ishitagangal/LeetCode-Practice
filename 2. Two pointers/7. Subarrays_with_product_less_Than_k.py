class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        if k <=1 :
            return 0
        num_of_sub_arrays = window_start = 0
        for window_end, val in enumerate(nums):
            product *= val
            while product >= k:
                product /= nums[window_start]
                window_start += 1
            num_of_sub_arrays += window_end - window_start + 1 
            #the number of new sub-arrays which gets generated on addition
            # of element are equal to the number of elements in the array.
        
        return num_of_sub_arrays