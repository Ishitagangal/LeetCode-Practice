class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        mini = nums[0]
        maxi = nums[0]
        result = maxi
        
        for i in range(1, len(nums)):
            current = nums[i]
            temp_maxi = max(current, maxi*current, mini*current)
            mini = min(current, maxi*current, mini*current)
            
            maxi = temp_maxi
            result = max(result, maxi)
        return result