class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2): return False 
        return self._isScramble(s1, s2) or self._isScramble(s1, "".join(list(reversed(s2))))
        
    def _isScramble(self, s1, s2):
        # print 'check', s1, s2
        if s1 == s2: return True
        CC = {}
        for i, (c1, c2) in enumerate(zip(s1, s2)):
            if i == len(s1) - 1:
                return False 

            CC[c1] = CC.get(c1, 0) + 1
            if CC[c1] == 0: del CC[c1]
            CC[c2] = CC.get(c2, 0) - 1
            if CC[c2] == 0: del CC[c2]
            if not CC:
                return self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:])
                    
        return False 
        
print Solution().isScramble("abb", "bab")