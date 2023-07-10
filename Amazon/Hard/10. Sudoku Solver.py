class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, x, y, num):
            for i in range(9):
                if board[i][y] == num:
                    return False
            for j in range(9):
                if board[x][j] == num:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x//3)*3+i][(y//3)*3+j] == num:
                        return False
            return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for char in '123456789':
                        if is_valid(board, i, j, char):
                            board[i][j] = char
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

