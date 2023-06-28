class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

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
            
                

## Word Break 1
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def backtrack(s, wordDict, memo):
            if s in memo:
                return memo[s]
            if s in wordDict:
                return True
            memo[s] = False
            for i in range(1, len(s)):
                prefix = s[:i]
                suffix = s[i:]
                if prefix in wordDict and backtrack(suffix,wordDict,memo):
                    memo[s] = True
                    break
                elif suffix in wordDict and backtrack(prefix, wordDict, memo):
                    memo[s] = True
                    break
            return memo[s]
        return backtrack(s, wordDict, {})
        