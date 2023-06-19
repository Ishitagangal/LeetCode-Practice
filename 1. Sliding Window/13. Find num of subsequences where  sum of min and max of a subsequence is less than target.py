# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the 
# sum of the minimum and maximum element on it is less or equal to target. 
# Since the answer may be too large, return it modulo 109 + 7.
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        mod = 10**9 + 7
        left, right = 0, len(nums) - 1
        while left<=right:
            if nums[left] + nums[right] <= target:
                result = result+ pow(2, right - left, mod)
                left += 1
            else:
                right -=1
        return result % mod