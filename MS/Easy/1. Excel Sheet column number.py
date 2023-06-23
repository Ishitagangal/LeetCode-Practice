class Solution:
    # right to left
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        mapping = {chr(i + 65): i+1 for i in range(26)}
        
        string_length = len(columnTitle)
        for i in range(string_length):
            read_character = columnTitle[string_length - i - 1]
            result += mapping[read_character] * (26 **i)
        return result
    
    # left to right, same as for numbers but base 26 instead of 10
    def titleToNumber(self, columnTitle:str) -> int:
        result = 0
        n = len(columnTitle)
        for i in range(n):
            result = result * 26 + (ord(columnTitle[i]) - ord('A') + 1)
        return result