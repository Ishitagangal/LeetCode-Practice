class Solution:
    # store value at start index and (-value) at end + 1 index, take prefix sums and every index
    # in the middle will be updated by the value and the negative updated after range will zero out.
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length
        for update in updates:
            start, end, val = update[0], update[1], update[2]
            result[start] += val
            if end < length - 1:
                result[end + 1] -= val
        
        prefix = 0
        for i in range(length):
            prefix += result[i]
            result[i] = prefix
        return result