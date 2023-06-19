class Solution:
    # BFS from each point, and calculate distance but it takes O(m^2 n^2) time
    # Find median of rows, find median of columns, this r, c is median pt and calc.distance
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        rows, cols = self.get_building_points(grid)
        row, col = self.get_median_coordinates(rows, cols)
        result = 0
        for r in rows:
            result += abs(row -r)
        for c in cols:
            result += abs(col - c)
        
        return result
    
    def get_median_coordinates(self, rows, cols) -> Tuple[int, int]:
        # rows.sort() no need to sort since we collected rows and cols in sorted order
        # cols.sort()
        row, col = rows[len(rows)//2], cols[len(cols)//2]
        return row, col
    
    def get_building_points(self, grid) -> Tuple[List, List]:
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
        
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                if grid[i][j] == 1:
                    cols.append(j)
        return rows, cols
    

    