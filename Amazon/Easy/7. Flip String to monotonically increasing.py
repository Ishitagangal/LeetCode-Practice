class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zeroes = 0 # flip 0 to 1, but update it as min of ones, flips
        ones = 0
        flips = 0
        for char in s:
            if char == '1':
                ones +=1
            else:
                zeroes += 1
            zeroes = min(zeroes, ones)
        return zeroes