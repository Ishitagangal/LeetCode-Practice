class Solution:
# We need an array last[char] -> index of S where char occurs last.
# Then, let anchor and j be the start and end of the current partition.
# If we are at a label that occurs last at some index after j, we'll extend the partition j = last[c]. 
# If we are at the end of the partition (i == j) then we'll append a partition size to our answer, 
# and set the start of our new partition to i+1.
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c:i for i, c in enumerate(s)}
        start = end = 0
        result = []
        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.