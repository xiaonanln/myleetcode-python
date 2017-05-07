
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0: return []
        if n == 1: return [[1]]
        
        matrix = [None] * n
        for i in xrange(n):
            matrix[i] = [None] * n
        
        x, y = 0, 0
        dirx, diry = 1, 0
        
        minrow = 0
        maxrow = len(matrix) - 1
        mincol = 0
        maxcol = len(matrix[0]) - 1
        
        matrix[x][y] = 1
        nextval = 2
        
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
            matrix[y][x] = nextval
            nextval += 1
        
        return matrix 

print Solution().generateMatrix(1)
print Solution().generateMatrix(2)
print Solution().generateMatrix(3)
