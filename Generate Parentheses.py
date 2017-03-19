class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        self.n = n
        self.now = []
        self.depth = 0
        self.used_left = 0
        self.result = []
        
        self.solve()
        
        return self.result
        
    def solve(self):
        
        if self.depth == 0 and self.used_left == self.n:
            self.result.append( ''.join(self.now ))
            return 
        
        if self.used_left < self.n:
            self.now.append('(')
            self.depth += 1
            self.used_left += 1
            
            self.solve()
            
            self.depth -= 1
            self.used_left -= 1
            del self.now[-1]
        
        if self.depth > 0:
            self.now.append(')')
            self.depth -= 1
            
            self.solve()
            
            self.depth += 1
            del self.now[-1]
        
print Solution().generateParenthesis(1)
print Solution().generateParenthesis(2)
print Solution().generateParenthesis(3)
print Solution().generateParenthesis(4)