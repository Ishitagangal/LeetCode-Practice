# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        celebrity_candidate = 0
        for i in range(1, n):
            if knows(celebrity_candidate, i):
                celebrity_candidate=i # celebrity can't know i, if they do then they weren't it
        
        # confirm that our candidate is indeed the celebrity
        if self.is_celebrity(celebrity_candidate):
            return celebrity_candidate
        return -1
    
    def is_celebrity(self, candidate):
        for j in range(self.n):
            if candidate ==j:
                continue
            if knows(candidate, j) or not knows(j, candidate):
                return False
        return True