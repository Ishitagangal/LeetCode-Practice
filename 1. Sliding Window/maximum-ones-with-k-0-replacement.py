class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_of_zeroes = 0
        max_len = 0
        window_start = 0

        for window_end in range(len(nums)):
            if nums[window_end] == 0:
                num_of_zeroes += 1
            
            while num_of_zeroes > k:
                if nums[window_start] == 0:
                    num_of_zeroes -= 1
                window_start +=1
            max_len = max(max_len, window_end - window_start +1)
        return max_len