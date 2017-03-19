class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if not prices: return 0
        value = prices[0]
        pro = 0
        for i in xrange(1, len(prices)):
            if prices[i] >= value:
                pro += prices[i] - value
                value = prices[i]
            else:
                value = prices[i]
        
        return pro