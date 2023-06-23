class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        cur_sum = sum(rolls)
        missing_sum = mean * (m+n) - cur_sum
        if missing_sum < n or missing_sum > 6*n:
            return []
        part = missing_sum // n
        remainder = missing_sum % n
        result = [part] * n
        for i in range(remainder):
            result[i] += 1
        return result