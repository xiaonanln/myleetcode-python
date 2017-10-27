class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        self.m = m
        self.n = n
        self.x = 0
        self.y = 0
        self.count = 0
        self.answers = {}
        
        return self.solve(m, n)
    
    def solve(self, m, n):
        if (m, n) in self.answers:
            return self.answers[(m, n)]
        else:
            ans = self.real_solve(m, n)
            self.answers[(m, n)] = ans
            return ans
    
    def real_solve(self, m, n):
        if m == 1 or n == 1: return 1
        return self.solve(m-1, n) + self.solve(m, n-1)
    
#     def solve(self):
#         if self.x == self.m - 1 and self.y == self.n-1: 
#             self.count += 1
#             return 
#     
#         if self.x < self.m - 1:
#             self.x += 1
#             self.solve()
#             self.x -= 1
#         
#         if self.y < self.n - 1:
#             self.y += 1
#             self.solve()
#             self.y -= 1
#         
#         
        

print Solution().uniquePaths(1, 1)    
print Solution().uniquePaths(3, 7)
print Solution().uniquePaths(100,100)