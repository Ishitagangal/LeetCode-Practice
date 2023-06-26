class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def get_next_chunk(version, n, p) -> List[int]:
            if p > n -1:
                return 0, p
            
            p_end = p
            while p_end<n and version[p_end] != '.':
                p_end += 1
            
            if p_end != n-1:
                i = int(version[p:p_end])
            else:
                i = int(version[p:n])
            
            p = p_end + 1
            return i, p
        
        p1 = p2 = 0
        n1, n2 = len(version1), len(version2)

        while p1 < n1 or p2 < n2:
            i1, p1 = get_next_chunk(version1, n1, p1)
            i2, p2 = get_next_chunk(version2, n2, p2)
            if i1 != i2:
                return 1 if i1 > i2 else -1
            
        return 0