class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        def count_set_bits(n):
            count = 0
            while n:
                count += n &1
                n= n>>1
            return count
        
        bit_freq = collections.defaultdict(int)
        for num in set(nums):
            bits = count_set_bits(num)
            bit_freq[bits] +=1
        
        result = 0
        for i in range(1,30):
            for j in range(1,30):
                if i+j >= k:
                    result += bit_freq[i] * bit_freq[j]
        return result