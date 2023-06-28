class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        N = len(num1) + len(num2)
        result = [0] * N

        first = num1[::-1]
        second = num2[::-1]

        for p1, dig1 in enumerate(second):
            for p2, dig2 in enumerate(first):
                place = p1 + p2
                prod = int(dig1) * int(dig2)
                prod += result[place] # add to previous multiplication result in that pos

                result[place] = prod %10
                result[place+1] += prod//10 # carry
        
        if result[-1] == 0:
            result.pop()
        return ''.join(str(dig) for dig in reversed(result))