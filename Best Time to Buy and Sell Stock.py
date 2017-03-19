class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices: return 0
        
        minprices = [None] * len(prices)
        minprices[0] = prices[0]
        for i in xrange(1, len(prices)):
            minprices[i] = min(minprices[i-1], prices[i])
        
        maxp = 0
        for i, price in enumerate(prices):
            mp = minprices[i]
            maxp = max(maxp,  price - mp)
        
        return maxp
    
# print Solution().maxProfit([2,1,2,0,1]) 
print Solution().maxProfit([2, 1])