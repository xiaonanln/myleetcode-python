
class Solution(object):
	def maxProfit(self, prices, fee):
		"""
		:type prices: List[int]
		:type fee: int
		:rtype: int
		"""
		clear, hold = 0, float('-inf')
		for price in prices:
			# the i-1 day is passed
			clear, hold = max(clear, hold + price - fee), max(clear - price, hold)

		return clear

print Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)