class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        signs = ["+", "-"]
        exponents = ["e", "E"]
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in signs:
                if i>0 and s[i-1] not in exponents:
                    return False
            elif c in exponents:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False
        return seen_digit