class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}
        def backtrack(s, wordDict, memo):
            if s in memo:
                return memo[s]
            if not s:
                return []
            if s in wordDict:
                return [s]
            result = []
            for i in range(1, len(s)):
                prefix = s[:i]
                suffix = s[i:]
                if prefix in wordDict:
                    res_rest = backtrack(suffix,wordDict,memo)
                    for word in res_rest:
                        result.append(prefix + ' ' + word)
            memo[s] = result
            return memo[s]
        return backtrack(s, wordDict, {})
            
                