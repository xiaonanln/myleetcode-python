class Solution(object):
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		neg_inf = float('-inf')
		H, C = [neg_inf, neg_inf], [neg_inf, neg_inf]

		for p in prices:
			H, C = ([max(H[0], 0 - p), max(H[1], C[0] - p)],
			        [max(C[0], H[0] + p), max(C[1], H[1] + p)])

		return max(0, *C)

print Solution().maxProfit([])
