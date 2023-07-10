class Solution:
    def minimumKeypresses(self, s: str) -> int:
        char_freq = defaultdict(int)
        for letter in s:
            char_freq[letter] += 1
        
        result, position = 0, 0
        # most freq char places at 1st position if possible
        # then incrememnt position if more characters
        frequencies = sorted(char_freq.values(), reverse=True)
        for index, freq in enumerate(frequencies):
            if index % 9 == 0: # position of this char is at 2nd place on the dialer now, then 3rd etc
                position += 1
            result += position *freq # number of times this char would be pressed is its frequency times its position on the dialer
        return result