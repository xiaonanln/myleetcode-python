# Given two binary strings, return their sum (also a binary string).
# 
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        
        sums = {
            "00": ("0", "0"),
            "01": ("1", "0"),
            "10": ("1", "0"),
            "11": ("0", "1"), 
        } 
        
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        if len(b) < len(a):
            b = "0" * (len(a) - len(b)) + b 
            
        result = []
        c = "0"
        for i in xrange(len(a) - 1, -1, -1):
            v = a[i] + b[i]
            v, c1  = sums[v]
            v, c2 = sums[v + c]
            result.append(v)
            c = "1" if c1 == '1' or c2 == '1' else "0"
        
        if c == '1':
            result.append(c)
            
        return ''.join(reversed(result))
        
    
sol = Solution()
print sol.addBinary("11", "1")