class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in result_dict:
                return [i, result_dict[target - nums[i]]]
            else:
                result_dict[nums[i]] = i