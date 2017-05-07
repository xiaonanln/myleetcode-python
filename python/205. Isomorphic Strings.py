class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        M = [None] * 256
        RM = [None] * 256
        for c1, c2 in zip(s, t):
        	m = M[ord(c1)]
        	if m == c2: continue 

        	rm = RM[ord(c2)]
        	if rm is not None: return False 

        	if m is None: 
        		M[ord(c1)] = c2
        		RM[ord(c2)] = c1
        	else: 
        		return False

        return True 

print Solution().isIsomorphic("ab", "ca")
# print Solution().isIsomorphic("egg", "add")
# print Solution().isIsomorphic("foo", "bar")
# print Solution().isIsomorphic("paper", "title")
