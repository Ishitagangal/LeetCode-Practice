class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root, 0)
    
    def search_helper(self, word, node, index) -> bool:
        if index == len(word):
            return node.is_end
        char = word[index]
        if char != ".":
            return char in node.children and self.search_helper(word, node.children[char], index + 1)
        for char in node.children:
            if self.search_helper(word, node.children[char], index+1):
                return True
        return False
    
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)