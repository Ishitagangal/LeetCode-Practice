class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []

        def backtrack(s, index, path, result):
            if index > 4:
                return
            if index == 4 and not s:
                self.result.append(path[:-1])
            for i in range(1, len(s) + 1):
                if s[:i] == '0' or (s[0]!='0' and 0 < int(s[:i])<256):
                    backtrack(s[i:], index + 1, path + s[:i] + ".", self.result)
        
        backtrack(s, 0, "", self.result)
        return self.result