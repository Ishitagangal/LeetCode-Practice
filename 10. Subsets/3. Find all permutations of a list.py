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
