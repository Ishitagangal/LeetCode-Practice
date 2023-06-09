class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        result = []
        for i in range(n -1, -1, -1):
            if a[i] == '1':
                carry +=1
            if b[i] == '1':
                carry+=1
            if carry %2 == 0:
                result.append('0')
            else:
                result.append('1')
            carry = carry // 2
        if carry == 1:
            result.append('1')
        return ''.join(reversed(result))