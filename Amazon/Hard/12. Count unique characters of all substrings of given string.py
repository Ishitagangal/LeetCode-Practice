class Solution:
    # https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/solutions/129021/o-n-java-solution-dp-clear-and-easy-to-understand/
    def uniqueLetterString(self, s: str) -> int:
        # or set last index to -1 and use (last_index[char] - 1) in contrib calc
        last_index = {c:0 for c in s}
        contributions = {c:0 for c in s}
        result = 0

        for i, char in enumerate(s):
            substrings_ending_here = i+1
            contributions[char] = substrings_ending_here - last_index[char]
            cur  = 0
            # calculate new contributon to unique substrings after this new char is added
            for contrib in contributions:
                cur+= contributions[contrib]
            result += cur
            last_index[char] = i +1
        return result
            