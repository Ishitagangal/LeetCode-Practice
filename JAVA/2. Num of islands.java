class Solution {
  public int numIslands(char[][] grid) {
    if (grid == null || grid.length == 0) {
      return 0;
    }
    int count = 0;
    for(int i = 0; i< grid.length; i++){
        for(int j = 0; j<grid[0].length; j++){
            if(grid[i][j] == '1'){
                bfsFill(grid, i, j);
                count++;
            }
        }
    }
    return count;
  }

  private void bfsFill(char[][] grid, int r, int c){
      int [][] directions = {{0,1}, {1,0}, {0, -1}, {-1,0}};
      grid[r][c] = '0';
      int nr = grid.length;
      int nc = grid[0].length;
      Queue<Integer> queue = new LinkedList<Integer>();
      int code = r*nc + c;
      queue.offer(code);
      while(!queue.isEmpty()){
          code = queue.poll();
          int i = code/nc;
          int j = code%nc;
          for(int[] dir : directions){
              int new_row = i + dir[0];
              int new_col = j + dir[1];
              
              if(0<=new_row && new_row<nr && 0<=new_col && new_col<nc && grid[new_row][new_col] == '1'){
                  grid[new_row][new_col] = '0';
                  queue.offer(new_row*nc + new_col);
              }
          }
      }


  }
}