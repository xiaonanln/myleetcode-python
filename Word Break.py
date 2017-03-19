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
    
class SolutionOld: # DP
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
        

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        #define dp[i][j] = s[i:j] can be break
        N = len(s)
        dp = [[None]*(N+1) for _ in xrange(N+1)]
        for L in xrange(1, N+1): # for each substring length
            for i in xrange(0, N-L +1):
                j = i+L
                if s[i:j] in wordDict:
                    dp[i][j] = True 
                else:
                    dp[i][j] = False
                    for k in xrange(i+1, j):
                        # print N, i, L, j, k
                        if dp[i][k] and dp[k][j]:
                            dp[i][j] = True 
                            break 

        return dp[0][N]
    
print Solution().wordBreak("leetcode", ["leet", "code"])
print Solution().wordBreak("a", ["a"])
print Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])



























