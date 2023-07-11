class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        min_len = len(str(low))
        max_len = len(str(high))
        nums = []
        for length in range(min_len, max_len+1):
            for i in range(10 - length):
                num = int(sample[i:i+length])
                if num >= low and num <= high:
                    nums.append(num)
        return nums