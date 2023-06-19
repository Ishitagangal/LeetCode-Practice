class Solution:
    # just find the length of shortest path
    # can also do bi-directional search from begin and end word simultaneously
    # so we reach the answer faster than single BFS
    # O(M^2 * N) with M is length of each word, N is num of words
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        L = len(beginWord)
        
        all_combo_dict = collections.defaultdict(list)
        
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)
        
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord:True}
        
        while queue:
            currentWord, level = queue.popleft()
            # create new generic word for each letter in word, go through created dict values for this new key word to see if we have found an end word, if not add them to visited and append to queue
            for i in range(L):
                intermediate = currentWord[:i] + "*" + currentWord[i+1:]
                for word in all_combo_dict[intermediate]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                # all_combo_dict[intermediate] = []
        return 0

## WORD LADDER 2
## find the path fromsource to destination and all possible combinations of 
## ways to get to the result/transaformation
## Hit -> hot -> cot -> cog
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.adj_map = defaultdict(set)
        result = []

        if endWord not in wordList: 
            return []
        
        #build_adjacency_map
        self.bfs(beginWord, set(wordList))
        
        self.traverse_and_backtrack(beginWord, endWord, [beginWord], result)
        return result
        
        
    def findNeighbors(self, cur_word, word_list):
        neighbors = set()
        for i in range(len(cur_word)):
            for char in 'qwertyuiopasdfghjklzxcvbnm':
                next_word = cur_word[:i]+char+cur_word[i+1:]
                if next_word in word_list:
                    neighbors.add(next_word)
        return neighbors
    
        
    def bfs(self, begin_word, word_list):
        queue = deque()
        queue.append(begin_word)

        while queue:
            visited = set()
            word_list -=set(queue)
            layer_size = len(queue)
            for l in range(layer_size):
                cur_word = queue.popleft()
                neighbors = self.findNeighbors(cur_word, word_list) 
                for neighbor in neighbors:
                    self.adj_map[cur_word].add(neighbor)
                    queue.append(neighbor)
        
        
    def traverse_and_backtrack(self, source, dest, cur_path, result):
        if source == dest:
            result.append(cur_path.copy())
            
        if source not in self.adj_map:
            return
        
        for word in self.adj_map[source]:
            cur_path.append(word)
            self.traverse_and_backtrack(word, dest, cur_path, result)
            cur_path.pop() #backtrack
        