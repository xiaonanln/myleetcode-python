class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        
        return self.solve(S, 0)
    
    def solve(self, S, start):
        if start == len(S):
            return [[]]
        
        ss = self.solve(S, start+1)
        return ss + [ [S[start]] + s for s in ss]
    
        
    
S = Solution()
print S.subsets([1,2,3])