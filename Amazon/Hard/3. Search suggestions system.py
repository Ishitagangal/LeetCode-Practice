class Element(str):
    def __init__(self, word):
        self.word = word
    def __lt__(self, other):
        return self.word > other.word # max heap
    def __eq__(self, other):
        return self.word == other.word

class TrieNode:
    # store top 3 suggestions at each trie node
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.suggestion = [] # max heap

    def add_suggestion(self, product):
        heapq.heappush(self.suggestion, Element(product))
        if len(self.suggestion) > 3:
            heapq.heappop(self.suggestion)

    def get_suggestion(self):
        return sorted(self.suggestion, reverse = True)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        for prod in products:
            node = root
            for char in prod:
                node = node.children[char]
                node.add_suggestion(prod)
        
        result = []
        node = root
        for char in searchWord:
            node = node.children[char]
            result.append(node.get_suggestion())
        return result
