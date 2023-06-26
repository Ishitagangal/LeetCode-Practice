class Solution:
    # Finds ALL subarrays
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        result = 0
        sum_index = defaultdict(int) # sum, count of times it has appeared
        sum_index[0] = 1 # prefix sum 0 appears once at index 0 of array

        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in sum_index:
                result += sum_index[prefix_sum - k] # new prefix sum till old prefix sum (prefixsum-k) make up a a subarray. SO each time you see a sum, incrememnt value as it can possibly form a subarray
            sum_index[prefix_sum] +=1
            
        return result

# Max. Non overlapping subaraays where sum ==  target
# nonoverlapping is key, so maintain sum seen so far and once answer found reset seen dict
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = set([0])
        result = curr = 0

        for i, num in enumerate(nums):
            curr += num
            prev = curr - target
            if prev in seen:
                result += 1
                seen = set()
            seen.add(curr)
        return result

# Maximum size subaraay sum that equals k
class Solution:
    def maxSubArrayLen(self, nums: List[int], target: int) -> int:
        sum_to_index = collections.defaultdict(int)
        cur_sum = max_len = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum == target:
                max_len = max(max_len, i+1)
            elif cur_sum - target in sum_to_index:
                max_len = max(max_len, i - sum_to_index[cur_sum - target])
            
            if cur_sum not in sum_to_index:
                sum_to_index[cur_sum] = i
        return max_len
            