# find the number of index triplets i, j, k with 0 <= i < j < k < n 
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        result = 0
        nums.sort()
        
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < target:
                    result += right - left
                    left +=1
                else:
                    right -=1
        return result