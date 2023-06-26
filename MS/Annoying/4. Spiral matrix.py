
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)] # in order, R, Down, L, Up
        curr_dir = 0
        change_dir = 0 # when it becomes 2, we reached two visited cells and turned twice so done traversing
        row, col = 0, 0
        result = [matrix[0][0]]
        matrix [0][0] = True

        while change_dir < 2:
            # keep traversing until we need to change direction
            while True:
                next_row = row + directions[curr_dir][0]
                next_col = col + directions[curr_dir][1]

                if not(0<=next_row<rows and 0<=next_col<cols):
                    break
                
                if matrix[next_row][next_col] == True: # visited
                    break
                
                change_dir = 0 # no need to change dir so reset
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = True
            
            # after breaking from while true, change dir
            curr_dir = (curr_dir + 1) % 4
            change_dir +=1
        
        return result