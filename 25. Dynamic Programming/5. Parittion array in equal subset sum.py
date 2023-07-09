# Given an integer array nums, return true if you can partition the array into 
# two subsets such that the sum of the elements in both subsets is equal or false otherwise.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(nums, n, subset_sum, memo)->bool:
            if (nums, n, subset_sum) in memo:
                return memo[(nums, n, subset_sum)]
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = dfs(nums, n - 1, subset_sum - nums[n-1],memo) or dfs(nums, n - 1, subset_sum, memo)
            memo[(nums, n, subset_sum)] = result
            return result
        
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)
        memo = {}
        return dfs(tuple(nums), n, subset_sum, memo)