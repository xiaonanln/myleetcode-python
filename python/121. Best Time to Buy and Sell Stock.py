class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		minPrice = float('inf')
		maxProfit = 0
		for price in prices:
			maxProfit = max(maxProfit, price - minPrice)
			minPrice = min(minPrice, price)
		return maxProfit

print Solution().maxProfit( [7, 1, 5, 3, 6, 4])
print Solution().maxProfit([7, 6, 4, 3, 1])