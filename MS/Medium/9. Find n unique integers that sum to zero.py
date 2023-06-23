class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            result = []
        else:
            result = [0]
        max_val = n //2
        for i in range(1,max_val + 1):
            result.insert(0, -i)
            result.append(i)
        return result