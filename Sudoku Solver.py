class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        rowUsable = [set(xrange(1, 10)) for i in xrange(9)]
        colUsable = [set(xrange(1, 10)) for i in xrange(9)]
        blockUsable = [set(xrange(1, 10)) for i in xrange(9)]
        
        __board = board
        board = [ [ int(c) if c != '.' else None for c in row ] for row in board]
        
        for row in xrange(9):
            boardrow = board[row]
            
            for col in xrange(9):
                n = boardrow[col]
                if n is None: continue
                
                rowUsable[row].remove(n)
                colUsable[col].remove(n)
            
                blockindex = (row // 3) * 3 + (col // 3)
                blockUsable[blockindex].remove(n)
        
        self.rowUsable = rowUsable
        self.colUsable = colUsable
        self.blockUsable = blockUsable
        
        r, c = 0, 0
        self.solve(board, r, c)
        for i, row in enumerate(board):
            __board[i] = ''.join( str(n) for n in row)
        
    def solve(self, board, r, c):
        if c == 9: 
            c = 0
            r += 1
            if r == 9:
                return True
        
        if board[r][c] is None:
            bi = (r // 3) * 3 + (c // 3)
            usable = self.rowUsable[r] & self.colUsable[c] & self.blockUsable[bi]
            
#             if r == 1: print self.rowUsable[1], usable
            
            for n in usable:
#                 if r == 1: print 'using', n
                board[r][c] = n
                
                self.rowUsable[r].remove(n)
                self.colUsable[c].remove(n)
                self.blockUsable[bi].remove(n)
                
                if self.solve(board, r, c+1): return True
                
                board[r][c] = None
                self.rowUsable[r].add(n)
                self.colUsable[c].add(n)
                self.blockUsable[bi].add(n)
            
            return False
        else:
            return self.solve(board, r, c + 1)
    
E = '.'

# board = [
#     [5, 3, E, E, 7, E, E, E, E], 
#     [6, E, E, 1, 9, 5, E, E, E], 
#     [E, 9, 8, E, E, E, E, 6, E], 
#     [8, E, E, E, 6, E, E, E, 3], 
#     [4, E, E, 8, E, 3, E, E, 1], 
#     [7, E, E, E, 2, E, E, E, 6], 
#     [E, 6, E, E, E, E, 2, 8, E], 
#     [E, E, E, 4, 1, 9, E, E, 5], 
#     [E, E, E, E, 8, E, E, 7, 9], 
# ]

board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."] 
Solution().solveSudoku(board)

print '\n'.join(board)