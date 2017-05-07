class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0: return []
        if len(matrix[0]) == 0: return []
        
        x, y = 0, 0
        dirx, diry = 1, 0
        
        minrow = 0
        maxrow = len(matrix) - 1
        mincol = 0
        maxcol = len(matrix[0]) - 1
        
        R = [ matrix[y][x] ]
        
        while True:
            nx, ny = x + dirx, y + diry
            
            if nx < mincol or nx > maxcol or ny < minrow or ny > maxrow:
                if dirx == 1 and diry == 0:
                    dirx, diry = 0, 1
                    minrow += 1
                elif dirx == 0 and diry == 1:
                    dirx, diry = -1, 0
                    maxcol -= 1
                elif dirx == -1 and diry == 0:
                    dirx, diry = 0, -1
                    maxrow -= 1
                elif dirx == 0 and diry == -1:
                    dirx, diry = 1, 0
                    mincol += 1
                else:
                    assert False
                
#                 print minrow, maxrow, mincol, maxcol
                
                nx, ny = x + dirx, y + diry
                if nx < mincol or nx > maxcol or ny < minrow or ny > maxrow:
                    break
                
            x, y = nx, ny
            R.append( matrix[y][x] )
        
        return R                
            

print Solution().spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
