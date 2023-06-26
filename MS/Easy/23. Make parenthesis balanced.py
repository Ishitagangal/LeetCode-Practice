# Min. add to make them vallid
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need_left = need_right = 0
        for char in s:
            if need_right == 0 and char == ')':
                need_left += 1
            elif char == '(':
                need_right += 1
            else:
                need_right -=1
        return need_left + need_right

# Min insertions to make valid where ( should match ))
class Solution:
    def minInsertions(self, s: str) -> int:
        close_bracket = 0
        s = s.replace('))', '}')
        open_bracket = 0 # for 2 )) to be added
        add_open_bracket = 0 # if we have )) but no prior open bracket to match

        for char in s:
            if char == '(':
                open_bracket += 1
            else:
                if char == ')':
                    close_bracket +=1
                if open_bracket:
                    open_bracket -= 1
                else:
                    add_open_bracket +=1
        return add_open_bracket + close_bracket + 2 * open_bracket