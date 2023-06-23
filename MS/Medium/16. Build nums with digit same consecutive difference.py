class Solution:
    # O(2^n)
    # do bfs to find possibilities at each level
    # tree of depth n, each level one extra digit is added within k
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n ==1:
            return [i for i in range(10)]
        queue = [digit for digit in range(1, 10)]

        for level in range(n-1):
            next_level = []
            for num in queue:
                digit = num % 10
                next_digits = set([digit + k, digit - k]) # digit + or - k, to be added to make new num
                for next_digit in next_digits:
                    if 0 <= next_digit < 10:
                        new_num = num * 10 + next_digit
                        next_level.append(new_num)
            queue = next_level
        return queue


## DFS
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:

        if N == 1:
            return [i for i in range(10)]

        ans = []
        def DFS(N, num):
            # base case
            if N == 0:
                return ans.append(num)

            tail_digit = num % 10
            # using set() to avoid duplicates when K == 0
            next_digits = set([tail_digit + K, tail_digit - K])

            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    DFS(N-1, new_num)

        for num in range(1, 10):
            DFS(N-1, num)

        return list(ans)