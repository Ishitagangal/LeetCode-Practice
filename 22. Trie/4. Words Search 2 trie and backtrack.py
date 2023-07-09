# word search 2
class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False
        
class Solution:  
    def __init__(self):
        self.root = TrieNode()
        self.num_words = 0

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        self.num_words +=1
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
        rows = len(board)
        cols = len(board[0])        
        result = []
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in self.root.children:
                    self.backtracking(board, row, col, self.root, "", result)
        return result
    
    def backtracking(self, board, row, col, node, path, result):
        if self.num_words == 0:
            return
        if node.is_end:
            result.append(path[:])
            node.is_end = False # avoid duplicates
            self.num_words -=1
            
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return

        letter = board[row][col]
        if not letter in node.children or not node:
            return
        node = node.children[letter]
        
        board[row][col] = "#"
        self.backtracking(board, row+1, col, node, path+letter, result)
        self.backtracking(board, row-1, col, node, path+letter, result)
        self.backtracking(board, row, col+1, node, path+letter, result)
        self.backtracking(board, row, col-1, node, path+letter, result)
        board[row][col] = letter
        