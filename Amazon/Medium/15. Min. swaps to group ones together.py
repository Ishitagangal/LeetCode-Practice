class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = nums.count(1)
        n = len(nums)
        curr = 0
        ones_in_window = 0
        window_start = 0
        for window_end in range(n):
            # slide window forward, 
            if total_ones <= window_end and nums[window_end - total_ones] == 1:
                curr -= 1
                # incremeent window start, but we aren't calculating len so no need to
            if nums[window_end] == 1:
                curr += 1
            ones_in_window = max(ones_in_window, curr)
        return total_ones - ones_in_window