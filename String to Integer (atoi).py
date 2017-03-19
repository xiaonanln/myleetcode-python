class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        
        sign = 1
        start = 0
        if start < len(str) and str[start] in '+-':
            sign = -sign if str[start] == '-' else sign
            start = start + 1
        
        digits = '0123456789'
        p = start
        num = 0
        while p < len(str) and str[p] in digits:
            d = ord(str[p]) - ord('0')
            num = num * 10 + d
            p += 1
        
        num = num * sign
        if num > 2147483647: num = 2147483647
        if num < -2147483648: num = -2147483648
        return num
        
    
print Solution().atoi("")
print Solution().atoi("  1")
print Solution().atoi("  -1")
print Solution().atoi("  -1abc")
print Solution().atoi("  1231231249213412341234234")
print Solution().atoi("  ++1")