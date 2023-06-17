class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.backtrack(i, j, word):
                    return True
        
        return False
    
    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True
        
        if not (0<=row<self.ROWS and 0<=col<self.COLS) or self.board[row][col] != suffix[0]:
            return False
        
        flag = False
        self.board[row][col] = "#"
        for dir in [(0,1), (1, 0), (0, -1), (-1, 0)]:
            flag = self.backtrack(row + dir[0], col + dir[1], suffix[1:])
            if flag:
                break
        
        self.board[row][col] = suffix[0]
        return flag