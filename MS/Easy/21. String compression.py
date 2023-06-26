class Solution:
    def compress(self, chars: List[str]) -> int:
        first, second = 0, 0
        count = 0
        while second<len(chars):
            chars[first] = chars[second]
            count = 1

            while second + 1 < len(chars) and chars[second] == chars[second + 1]:
                second += 1
                count +=1
            if count > 1:
                for c in str(count):
                    chars[first + 1] = c
                    first += 1
            first += 1
            second += 1
        return first
