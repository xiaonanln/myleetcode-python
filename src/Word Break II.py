class Solution:
    
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        n = len(s)
        DP = [None] * (n + 1)
        DP[n] = [ (n, ) ] # DP[n] is set of all dividers
        
        for i in xrange(n-1, -1, -1):
            dp = []
            for j in xrange(i+1, n+1):
                subs = s[i:j]
                if DP[j] and subs in dict:
                    for _dp in DP[j]:
                        dp.append((i, ) + _dp)
            DP[i] = dp
        
        result = []
        for divs in DP[0]:
            sen = s[divs[0]:divs[1]]
            for i in xrange(1, len(divs)-1):
                sen += ' '
                sen += s[divs[i]:divs[i+1]]
            result.append(sen)
        
        return result
                
# s = "catsanddog"
# dict = ["cat", "cats", "and", "sand", "dog"]
# print Solution().wordBreak(s, dict)
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print Solution().wordBreak(s, dict)