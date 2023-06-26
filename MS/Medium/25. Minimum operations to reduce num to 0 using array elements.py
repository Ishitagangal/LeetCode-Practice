class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        cur_sum, max_len = 0, 0
        start = 0
        found = False
        for end in range(len(nums)):
            cur_sum += nums[end]
            while start <= end and cur_sum > target:
                cur_sum -= nums[start]
                start += 1
            if cur_sum == target:
                found = True
                max_len = max(max_len, end-start+1)
        return len(nums) - max_len if found else -1