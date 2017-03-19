import collections

class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board: return 
        if not board[0]: return 
        
        ROWS = len(board)
        COLS = len(board[0])
        
        live = [None] * ROWS
        for i in xrange(ROWS):
            live[i] = [False] * COLS
        
        q = collections.deque()
        visited = set()
        
        def marklive(x, y):
            if board[x][y] == 'X': return 
            if (x, y) in visited: return 
            
            live[x][y] = True
            q.append( (x, y) )
            visited.add( (x, y) )
        
        for i in xrange(ROWS):
            marklive(i, 0)
            marklive(i, COLS-1)
        for i in xrange(COLS):
            marklive(0, i)
            marklive(ROWS-1, i)
            
        while q:
            x, y = q.popleft()
            if x > 0: marklive(x - 1, y)
            if x < ROWS-1: marklive(x + 1, y)
            if y > 0: marklive(x, y - 1)
            if y < COLS-1: marklive(x, y + 1)
            
        for x in xrange(ROWS):
            for y in xrange(COLS):
                if board[x][y] == 'O' and not live[x][y]:
                    board[x][y] = 'X'
                     
    
board = [None] * 9
for i in xrange(9):
    board[i] = ['X'] * 9
# print board
print Solution().solve([])
print Solution().solve(board)