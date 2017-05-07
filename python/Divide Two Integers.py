class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if dividend < 0 and divisor < 0:
            return self.divide(-dividend, -divisor)
        elif dividend < 0:
            return -self.divide(-dividend, divisor)
        elif divisor < 0:
            return -self.divide(dividend, -divisor)
        
        __divisor = divisor
        r = 0
        while dividend and dividend >= __divisor:
            d = 1
            divisor = __divisor
            
            while dividend >= divisor + divisor:
                d += d
                divisor += divisor
            
            r += d
            dividend -= divisor
        
        return r
    
print Solution().divide(100, 1)
print Solution().divide(12, 4)
print Solution().divide(12, 13)