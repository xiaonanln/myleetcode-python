
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        rowIndex += 1
        if rowIndex == 0: return []
        row = [None] * rowIndex
        row[0] = 1
        for ri in xrange(1, rowIndex):
            fix = 0
            for col in xrange(1, ri + 1 - 1):
                prev = row[col]
                row[col] = row[col-1] - fix + prev
                fix = row[col] - prev
        
            row[ri] = 1
        
        return row
             
    
class Solution1:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0: return []
        rows = [None] * numRows
        rows[0] = [1] # row 1
        
        for i in xrange(2, numRows+1):
            rows[i-1] = self.makeNextRow(rows[i-2])
        return rows
    
    def makeNextRow(self, row):
        n = len(row)
        next_row = []
        next_row.append(row[0])
        for i in xrange(len(row)-1):
            next_row.append(row[i] + row[i+1])
        next_row.append(row[-1])
        return next_row
    
def show(S):
    print S
    

show( Solution().getRow(0))
show( Solution().getRow(1))
show( Solution().getRow(2))
show( Solution().getRow(3))
show( Solution().getRow(4))
show( Solution().getRow(5))