class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        table = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            table[i][0] = i
        for j in range(n+1):
            table[0][j] = j
        # 0,0 is an empty string hence the +1 for the table
        # first letter comparison is with 1st row/1st col
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = 1 + min(table[i-1][j], table[i][j-1], table[i-1][j-1])
        return table[-1][-1]

    # memoized
    def minDistanceMemoized(self, word1: str, word2: str) -> int:
        memo = {}
        return self.minDistanceHelper(word1, word2, 0, 0, memo)
    
    def minDistanceHelper(self, word1, word2, i, j, memo) ->int:
        if i == len(word1) and j ==len(word2):
            return 0
        if i == len(word1):
            return len(word2) - j # remaining letters of word2 must be added
        if j == len(word2):
            return len(word1) - i
        if (i, j) in memo:
            return memo[(i,j)]
        memo[(i,j)] = 0
        if word1[i] == word2[j]:
            result = self.minDistanceHelper(word1, word2, i+1, j+1, memo)
        else:
            insert = self.minDistanceHelper(word1, word2, i, j+1, memo)
            delete = self.minDistanceHelper(word1, word2, i+1, j, memo)
            replace = self.minDistanceHelper(word1, word2, i+1, j+1, memo)
            result = 1 + min(insert, replace, delete)
        memo[(i, j)] = result
        return memo[(i,j)]
        
        