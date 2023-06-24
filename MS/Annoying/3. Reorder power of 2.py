class Solution:
    # convert n to str and sort it 
    # then compare this to sorted string versions of poers of 2
    def reorderedPowerOf2(self, n: int) -> bool:
        c = collections.Counter(str(n))
        return any(c == collections.Counter(str(1 << i)) for i in range(30))