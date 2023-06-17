class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        s = S.lower()
        result = []

        def backtrack(combo=[], i=0):
            if len(combo) == len(S):
                result.append(list(combo))
            if i>=len(S):
                return
            if s[i].isdigit():
                combo.append(s[i])
                backtrack(combo, i+1)
                combo.pop()
            else:
                options = [s[i], s[i].upper()]
                for letter in options:
                    combo.append(letter)
                    backtrack(combo, i+1)
                    combo.pop()
        
        backtrack()
        return ["".join(word) for word in result]