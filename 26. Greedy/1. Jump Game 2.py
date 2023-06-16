class Solution:
    def jump_greedy(self, nums:List[int]) -> int: 
            if len(nums) <= 1: return 0
            left = 0
            right = nums[0]
            jumps = 1
            
            while right < len(nums) - 1:
                jumps +=1
                next_val = max(i+nums[i] for i in range(left, right+1))
                left, right = right, next_val
            
            return jumps