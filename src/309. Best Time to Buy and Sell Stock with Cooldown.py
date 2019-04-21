class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		B, S, C = float('-inf'), float('-inf'), 0
		for p in prices:
			# print p, B, S, C
			B, S, C = (
				max(B, C - p),
				B + p,
				max(S, C),
			)
			# print p, B, S, C


		return max(B, S, C)


print Solution().maxProfit([1,2,4])
# print Solution().maxProfit([1, 2, 3, 0, 2])
