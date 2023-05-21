class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_freq = Counter()
        window_start = window_size = 0
        max_len = 0

        for window_end, char in enumerate(s):
            char_freq[char] += 1
           
            while len(char_freq) > k: 
                # if length exceeds max distinct chars, drop chars from window start,
                # reduce freq count
                left_char = s[window_start]
                char_freq[s[window_start]] -= 1

                if char_freq[left_char] == 0:
                    del char_freq[left_char]
                window_start +=1
            
            window_size = window_end - window_start + 1
            max_len = max(max_len, window_size)

                
        return max_len
           
