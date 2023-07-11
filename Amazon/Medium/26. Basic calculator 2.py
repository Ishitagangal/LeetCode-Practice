class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return '0'
        stack = []
        num = 0
        sign = "+"
        i = 0
        lookup = {"+": 1, "-": -1}
        while i < len(s):
            char = s[i]
            if char.isdigit():
                num = int(char)
                while i < len(s) -1 and s[i+1].isdigit():
                    num = num * 10 + int(s[i+1])
                    i +=1
            if char in ("+", "-", "*", "/") or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = char
            i+=1
        return sum(stack)