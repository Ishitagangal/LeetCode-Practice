class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * m for _ in range(n)]

        for row in range(1, n):
            for col in range(1, m):
                d[row][col] = d[row - 1][col] + d[row][col - 1]

        return d[n - 1][m - 1]