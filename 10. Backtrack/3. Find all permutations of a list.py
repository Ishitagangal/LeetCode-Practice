class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start_index = 0):
            if start_index == n:
                result.append(list(nums))
                
            for i in range(start_index, n):
                nums[start_index], nums[i] = nums[i], nums[start_index]
                backtrack(start_index + 1)
                nums[start_index], nums[i] = nums[i], nums[start_index]
            
        n = len(nums)
        result = []
        backtrack( )
        return result

# OR
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
        
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
        ans = []
        backtrack([])
        return ans
