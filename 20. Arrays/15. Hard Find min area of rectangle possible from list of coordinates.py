# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel 
# to the X and Y axes. If there is not any such rectangle, return 0.
class Solution:
    # keep hashmap of all x coordinates to corresponding y coordinates as per input list
    # go through all points and for every point, look through remaining to determine if 
    # any y is in the map, it makes a rectangle
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        coordinate_map = collections.defaultdict(set)
        for point in points:
            coordinate_map[point[0]].add(point[1]) # x: set of y coordinates
        
        min_area = float(inf)
        for p1 in points:
            for p2 in points:
                if (p1[0] >= p2[0]) or (p1[1] >= p2[1]): # cant make rectangle
                    continue
                if p2[1] in coordinate_map[p1[0]] and p1[1] in coordinate_map[p2[0]]:
                    min_area = min(min_area, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
        
        return min_area if min_area < float(inf) else 0