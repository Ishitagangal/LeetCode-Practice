class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        first_negative_num = -1
        zero_position = -1
        negative_nums = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num < 0:
                negative_nums +=1
                if first_negative_num == -1:
                    first_negative_num = i
            if num == 0: # reset since anything before this ndex is useless in the subaray
                zero_position = i
                negative_nums = 0
                first_negative_num = -1
            else:
                if negative_nums % 2 == 0: # don't count zero if any
                    max_len = max(max_len, i - zero_position)
                else: # odd number o fnegative nums so don't count first negative number
                    max_len = max(max_len, i - first_negative_num)
        return max_len
                