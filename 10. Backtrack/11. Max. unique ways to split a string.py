class Solution:
    def maxUniqueSplitWorks(self, s: str) -> int:
        seen = set()
        def helper(s):
            result = 0
            for i in range(1, len(s) + 1):
                candidate = s[:i]
                if candidate not in seen:
                    seen.add(candidate)
                    result = max(result, 1 + helper(s[i:]))
                    seen.remove(candidate)
            return result
        return helper(s)

    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        result = 0
        length = len(s)
        def backtrack(count, index, seen):
            nonlocal result, length
            if index == length:
                result = max(result, count)
                return
            for i in range(index + 1, length + 1):
                candidate = s[index:i]
                if candidate not in seen:
                    seen.add(candidate)
                    backtrack(count + 1, i, seen)
                    seen.remove(candidate)
        backtrack(0, 0, seen)
        return result