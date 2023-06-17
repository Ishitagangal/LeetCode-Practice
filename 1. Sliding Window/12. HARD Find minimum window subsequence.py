# Given strings s1 and s2, return the minimum contiguous substring part of s1,
#  so that s2 is a subsequence of the part.
# If there is no such window in s1 that covers all characters in s2, return 
# the empty string "". If there are multiple such minimum-length windows, 
# return the one with the left-most starting index.
# Input: s1 = "abcdebdde", s2 = "bde"
# Output: "bcde"
# Explanation: 
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of s2 in the window must occur in order.
 
# Starting from left to find the starting index up till all chars in s2 match
# once we reach end of s2, start from right to left to find the minimum start index
# in s1. Use this to calculate minimum length, update start index for slicing
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        n = len(s1)
        m = len(s2)
        result = ""
        start = -1
        min_len = inf

        i = j = 0
        while i < (len(s1)):
            if s1[i] == s2[j]:
                j+=1
            if j == len(s2):
                curr_start = end = i # move right to left to find the start point
                while j > 0:
                    if s1[curr_start] == s2[j-1]:
                        j -=1
                    curr_start -=1
                if end - curr_start < min_len:
                    min_len = end - curr_start
                    start = curr_start + 1
                i = curr_start + 1 # reset i to where wefound the start of the subsequence
            i += 1
        return s1[start:start+min_len] if min_len < inf else ""