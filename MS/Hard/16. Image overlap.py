class Solution:
    # O(n^4) https://leetcode.com/problems/image-overlap/solutions/150504/python-easy-logic/
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a = []
        b = []
        sliding_patterns_count = collections.defaultdict(int)
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    a.append((i,j))
                if img2[i][j] == 1:
                    b.append((i,j))
        result = 0
        for p1 in a:
            for p2 in b:
                pattern = (p2[0]-p1[0], p2[1] - p1[1])
                sliding_patterns_count[pattern] += 1
                result = max(result, sliding_patterns_count[pattern])
        return result