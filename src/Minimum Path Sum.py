class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if not grid: return 0
        if not grid[0]: return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        DP = []
        for row in grid:
            DP.append( [None] * len(row) )
        
        DP[ROWS-1][COLS-1] = grid[ROWS-1][COLS-1]
        
        def compute(row, col):
            v = grid[row][col]
            
            down, right = None, None
            
            if row < ROWS-1:
                down = DP[row + 1][col] + v
                
            if col < COLS-1:
                right = DP[row][col+1] + v
            
            ms = None
            if down is None: ms = right 
            elif right is None: ms = down
            else: ms = min(down, right)
            DP[row][col] = ms 
        
        for col in xrange(COLS-2, -1, -1):
            compute(ROWS-1, col)
        
        for row in xrange(ROWS-2, -1, -1):
            for col in xrange(COLS-1, -1, -1):
                compute(row, col)
                
        return DP[0][0]

print Solution().minPathSum([   
        ])
print Solution().minPathSum([
            [1],   
        ])

print Solution().minPathSum([
            [1, 2, 3],
            [3, 2, 1],
            [0, 0, 0],   
        ])