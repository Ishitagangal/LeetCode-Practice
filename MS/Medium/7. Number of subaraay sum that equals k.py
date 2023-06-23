class Solution:
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
            