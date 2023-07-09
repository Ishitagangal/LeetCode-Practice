class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        words=[word,word[::-1]]
        n=len(word)
        # print(zip(*board))
        for B in board,zip(*board):
            print(f"B: {B}")
            for row in B:
                print(f"Row : {row}")
                q=''.join(row).split('#')
                print(q)
                for w in words:
                    for s in q:
                        if len(s)==n:
                            if all(s[i]==w[i] or s[i]==' ' for i in range(n)):
                                return True
        return False