class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = defaultdict() # mapping of character to index it was at
        window_start = window_size = 0
        max_len = 0

        for window_end, char in enumerate(s):
            if char in char_index:
                window_start = max(window_start, char_index[char] + 1) # move left window to skip the old repeating character
            char_index[char] = window_end
            max_len = max(max_len, window_end - window_start + 1)
        
        return max_len