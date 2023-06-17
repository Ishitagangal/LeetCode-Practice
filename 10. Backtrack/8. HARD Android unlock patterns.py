class Solution:
    def __init__(self):
        self.skip = {
            (1, 3) : 2, (3, 1) : 2,
            (1, 7) : 4, (7, 1) : 4,
            (3, 9) : 6, (9, 3) : 6,
            (7, 9) : 8, (9, 7) : 8,
            (1, 9) : 5, (9, 1) : 5,
            (2, 8) : 5, (8, 2) : 5,
            (3, 7) : 5, (7, 3) : 5,
            (4, 6) : 5, (6, 4) : 5
        }
        self.seen = set()

    def numberOfPatterns(self, m: int, n: int) -> int:
        valid_patterns = 0
        for i in range(m,n+1):
            self.seen = set([1])
            valid_patterns += self.dfs(1, i -1) * 4 # we need i length of pattern, where i is min m max n, -1 because digit "1" used, times 4 since 1, 3, 7, 9 will have same possibilities
            self.seen = set([2])
            valid_patterns += self.dfs(2, i -1) * 4
            self.seen = set([5])
            valid_patterns += self.dfs(5, i -1)
        return valid_patterns
    
    def dfs(self, cur_num, remaining_length):
        if remaining_length == 0:
            return 1
        result = 0
        for next_num in range(1, 10):
            if next_num not in self.seen and ((cur_num, next_num) not in self.skip or self.skip[(cur_num, next_num)] in self.seen):
                self.seen.add(next_num)
                result += self.dfs(next_num, remaining_length -1)
                self.seen.remove(next_num)
        return result
        