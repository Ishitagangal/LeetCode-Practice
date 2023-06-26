class Solution:
    def maxLength(self, A):
        combinations = [set()]
        for word in A:
            if len(set(word)) < len(word): continue
            word = set(word)
            for combo in combinations[:]:
                if word & combo: continue
                combinations.append(word | combo) # combine sets if unique and add to result
        return max(len(string) for string in combinations)