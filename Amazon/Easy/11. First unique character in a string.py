class Solution:
    def firstUniqChar(self, s: str) -> int:
        index_char = [-1] *  26
        for i, char in enumerate(s):
            if index_char[ord(char) - ord('a')] == -1:
                index_char[ord(char) - ord('a')] = i
            elif index_char[ord(char) - ord('a')] >= 0:
                index_char[ord(char) - ord('a')] = -2
        
        result = float('inf')
        for i in range(0, 26):
            if index_char[i] >=0:
                result = min(result, index_char[i])

        return result if result != float('inf') else -1


    def firstUniqCharHashMap(self, s: str) -> int:
        seen = set()
        count = collections.Counter(s)
        for index, char in enumerate(s):
            if count[ch] == 1:
                return index
        return -1