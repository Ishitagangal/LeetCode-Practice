class Solution:
    # 1 pass
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        # binary search on entire matrix
        left, right = 0, m*n - 1
        while left<=right:
            mid = (left + right) // 2
            number = matrix[mid // n][mid % n]
            if target == number:
                return True
            elif target < number:
                right = mid - 1
            else:
                left = mid + 1
        return False

    # 2 passes, find row first and then binary search
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        row = -1
        for i in range(m):
            if target <= matrix[i][n-1]:
                row = i
                break
        if row == -1: return False
        arr = matrix[row]
        left, right = 0, n - 1
        while left<=right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif target < arr[mid]:
                right = mid -1
            else:
                left = mid + 1
        return False