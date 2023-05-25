class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = Counter({c:0 for word in words for c in word})

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c!=d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:
                if len(second_word) < len(first_word): return ""
        
        zero_degrees = deque([c for c in in_degree if in_degree[c] == 0])
        output = []
        while zero_degrees:
            char = zero_degrees.popleft()
            output.append(char)
            for letter in adj_list[char]:
                in_degree[letter] -= 1
                if in_degree[letter] == 0:
                    zero_degrees.append(letter)
        
        if len(output) < len(in_degree):
            return ""
        return "".join(output)