class Solution:
    # move max element to n-1 and min element to 0th with adjacent swaps
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        max_index = n -1
        min_index = 0
        for i in range(1, n):
            if nums[max_index] < nums[n-i-1]:
                max_index = n - i - 1
            if nums[min_index] > nums[i]:
                min_index = i
        swaps_for_min = min_index - 0
        swaps_for_max = n - 1 - max_index
        if min_index > max_index: # one overlapping swap so subtract it
            return  swaps_for_max + swaps_for_min - 1
        else:
            return swaps_for_max + swaps_for_min