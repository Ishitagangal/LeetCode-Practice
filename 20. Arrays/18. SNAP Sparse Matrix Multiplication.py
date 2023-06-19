class Solution:
    def multiplyNaive(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for i, row in enumerate(mat1):
            for k, row_num in enumerate(row):
                if row_num != 0:
                    for j, col_num in enumerate(mat2[k]):
                        result[i][j] += row_num * col_num
        
        return result
    
    def compress_matrix(self, matrix:List[List[int]]) ->List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        compressed = [[] for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] !=0:
                    compressed[row].append([matrix[row][col], col])
        return compressed

    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        A = self.compress_matrix(mat1)
        B = self.compress_matrix(mat2)

        for i in range(m):
            for num1, k in A[i]:
                for num2, j in B[k]:
                    result[i][j] += num1 * num2
        
        return result
    