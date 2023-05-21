class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = Counter()
        window_start = window_size = 0
        max_len = 0
        most_freq_char = 0 #keep count of frequency not the actual char

        for window_end, right_char in enumerate(s):
            char_freq[right_char] += 1
            # most_freq_char = max(most_freq_char, char_freq[right_char])
            most_freq_char = max(char_freq.values())

            window_size = window_end - window_start + 1
            letters_to_change = window_size - most_freq_char

            while window_end - window_start +1 - most_freq_char > k:
                char_freq[s[window_start]] -=1
                if char_freq[s[window_start]] == 0:
                    del char_freq[window_start]
                window_start += 1
            max_len = max(max_len, window_end - window_start +1)
        return max_len