class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = values[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if values[s[i]] < values[s[i+1]]:
                result -= values[s[i]]
            else:
                result += values[s[i]]
        return result

## Integer to roman

class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        result = []
        for val, symbol in digits:
            if num == 0:
                break
            count = num//val
            num = num % val
            result.append(symbol * count)
        return "".join(result)