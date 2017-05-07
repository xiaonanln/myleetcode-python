class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        
        CC = {}
        for i in xrange(26):
            CC[chr(ord('a') + i)] = 0
            CC[chr(ord('A') + i)] = 0
            
        start = 0
        curlen = 0
        maxlen = 0
        for i, c in enumerate(s):
            CC[c] += 1
            curlen += 1
            
            if CC[c] > 1:
                while s[start] != c:
                    CC[s[start]] -= 1
                    start += 1
                    curlen -= 1
                
                CC[s[start]] -= 1
                start += 1
                curlen -= 1
            
            maxlen = max(maxlen, curlen)
        
        return maxlen
                


print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("bbbbbbbbb")