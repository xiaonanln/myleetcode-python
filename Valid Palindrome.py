class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        def valid(c):
            if ord(c) >= ord('a') and ord(c) <= ord('z'): return True
            if ord(c) >= ord('A') and ord(c) <= ord('Z'): return True
            if ord(c) >= ord('0') and ord(c) <= ord('9'): return True
            return False
            
        s = ''.join( c.lower() for c in s if valid(c))
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1 
        return True
    
print Solution().isPalindrome('abccba')
print Solution().isPalindrome('ab cdba')