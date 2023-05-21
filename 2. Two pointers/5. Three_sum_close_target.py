class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left, right = i+1, len(nums) - 1
            
            while left<right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(target-sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    left +=1
                else:
                    right-=1
            if diff == 0:
                break
        return target - diff