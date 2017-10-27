class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        C = [0] * n
        S1 = [0] * (n * 2 - 1)
        S2 = [0] * (n * 2 - 1)
        
        RS = []
        R = []
        row = 0
        self.solve(n, 0, C, S1, S2, R, RS)
        return RS

    
    def solve(self, n, row, C, S1, S2, R, RS):
        if row == n:
            RS.append(
                ['.' * col + 'Q' + '.' * (n-col-1) for col in R]
            )
            return 
            
        for col in xrange(n):
            if C[col]: continue 
            if S1[col + row]: continue 
            if S2[(n-col-1) + row]: continue 
            
            C[col] = 1
            S1[col + row] = 1
            S2[(n-col-1) + row] = 1
            
            R.append(col)
            self.solve(n, row+1, C, S1, S2, R, RS)
            del R[-1]
            
            C[col] = 0
            S1[col + row] = 0
            S2[(n-col-1) + row] = 0

S = Solution()
print S.solveNQueens(1)
print S.solveNQueens(2)
print S.solveNQueens(3)
print S.solveNQueens(4)