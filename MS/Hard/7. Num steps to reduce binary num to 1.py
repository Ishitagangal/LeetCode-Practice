class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        carry = 0
        n = len(s)
        for i in range(n-1, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                result += 2 # two ops needed, add 1 and divide by 2
            else:
                result += 1 # one op needed, divide by 2
        return result + carry # if carry is 1 at the end, remaining 1 + carry is even so divide by 2