class SolutionTLE:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if s == '': return True
        
        return self.solve(s, 0, len(s), set(dict))
    
    def solve(self, s, start, stop, dict):
        if s in dict: return True
        
        for i in xrange(stop-1, start, -1):
            left = s[start:i]
            if left in dict:
                if self.solve(s, i, stop, dict): return True
                
        return False
    
class Solution: # DP
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        DP = [False] * (n+1) # DP[i] ==> if s[i:] can be breaked into words, so 0 <= i <= len(s), and DP[0] is the answer
        
        DP[n] = True
        for i in xrange(n-1, -1, -1):
            can = False
            for j in xrange(i+1, n+1):
                subs = s[i:j]
                if subs in dict:
                    can = DP[j]
                    if can: break
            
            DP[i] = can
        
        return DP[0]
        
        
    
print Solution().wordBreak("leetcode", ["leet", "code"])
print Solution().wordBreak("a", ["a"])
print Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])



























