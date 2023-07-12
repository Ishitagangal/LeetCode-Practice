class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 0001111 -> prev_group = 3, cur_group = 4
        prev_group = 0 
        cur_group = 1 # start iteration from 1st index,
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur_group += 1
            else:
                prev_group = cur_group
                cur_group = 1
            if prev_group >= cur_group:
                result += 1# 0001, result = 1 -> "01", 00011, result = 2 -> "0011"...
        return result