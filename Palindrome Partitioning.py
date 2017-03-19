class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
#         print len(s)
        indexes = {}
        for i, c in enumerate(s):
            if c not in indexes:
                indexes[c] = []
            
            indexes[c].append(i)
            
        self.indexes = indexes
            
        return self.solve(s, 0, len(s))
        
    def solve(self, s, start, stop):
        if stop <= start:
            return [ [] ]
        if stop == start + 1:
            return [ [s[start:stop]] ]
         
        result = []
        c = s[start]
        inds = self.indexes[c]
        
        for ind in inds:
            if ind < start : continue
            
            part = s[start:ind+1]
            if not self.ispalindrome(part): continue
            
            sols = self.solve(s, ind+1, stop) 
#             print part, left, sols
#             print part, s[ind+1:], sols
            for sol in sols:
                result.append( [part] + sol )
        
        return result
    
    def ispalindrome(self, word):
        lw = list(word)
        return lw == list(reversed(lw))

print Solution().partition("a")    
print Solution().partition("aba")
print Solution().partition("ltsqjodzeriqdtyewsrpfscozbyrpidadvsmlylqrviuqiynbscgmhulkvdzdicgdwvquigoepiwxjlydogpxdahyfhdnljshgjeprsvgctgnfgqtnfsqizonirdtcvblehcwbzedsmrxtjsipkyxk")
