class Solution:
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
    for r in S:
        print r
    

show( Solution().generate(0))    
show( Solution().generate(1))
show( Solution().generate(2))
show( Solution().generate(3))
show( Solution().generate(4))
show( Solution().generate(5))