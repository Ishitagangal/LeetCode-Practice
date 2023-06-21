class TicTacToe:
    def __init__(self, n: int):
        self.row=[0]*n
        self.col=[0]*n
        self.diag1=0
        self.diag2=0
        self.n=n

    def move(self, row: int, col: int, player: int) -> int:
        current_player = 1 if player == 1 else -1
        self.row[row]+= current_player
        self.col[col]+= current_player
        if row+col==self.n-1:
            self.diag1+= current_player
        if row-col==0:
            self.diag2+= current_player
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n \
            or abs(self.diag1)==self.n or abs(self.diag2)==self.n:
            return player
        return 0      


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)