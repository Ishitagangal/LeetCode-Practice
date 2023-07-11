class Solution:
    def minSwaps(self, s: str) -> int:
        #count number of characters in the wrong position
        def count_swaps(correct_char):
            result = 0
            for char in s:
                if char != correct_char:
                    result += 1
                correct_char = '1' if correct_char == '0' else '0' # switch correct char for next letter
            return result // 2

        ones = s.count('1')
        zeroes = len(s) - ones
        if abs(ones - zeroes) > 1: # difference can't be larger than 1 for alternating string
            return -1
        if ones > zeroes: # string must start with 1
            return count_swaps('1')
        elif zeroes > ones:
            return count_swaps('0')
        else: # if both are equal could start string wiht either so find min of both 
            return min(count_swaps('0'), count_swaps('1'))