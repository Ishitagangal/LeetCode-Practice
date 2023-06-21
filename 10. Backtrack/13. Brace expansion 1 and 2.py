class Solution:
    def expand(self, s: str) -> List[str]:
        self.result = []
        def backtrack(s, word):
            if not s:
                self.result.append(word)
            else:
                if s[0] == '{':
                    index = s.find('}')
                    for letter in s[1:index].split(","):
                        backtrack(s[index+1:], word+letter)
                else:
                    backtrack(s[1:], word + s[0])
        backtrack(s, "")
        self.result.sort()
        return self.result

class Solution:
    #  {a,b}{c,{d,e}} ["ac","ad","ae","bc","bd","be"]
    # stack = ['', [a, b], [c], []]
    # res =[d] , cur =[
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        result = []
        curr = []
        for i in range(len(expression)):
            char = expression[i]
            if char.isalpha():
                curr = [c+char for c in curr or ['']]
            elif char == '{':
                stack.append(result)
                stack.append(curr)
                result, curr = [], []
            elif char == '}':
                prev_curr = stack.pop()
                prev_result = stack.pop()
                curr = [b+a for a in (result + curr) for b in prev_curr or ['']]
                result = prev_result # restore previous result
            elif char == ',':
                result += curr
                curr = []
        return sorted(set(result + curr))