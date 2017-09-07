def mdarray(initVal, *dims): return [initVal] * dims[0] if len(dims) == 1 else [ mdarray(initVal, *dims[1:]) for _ in xrange(dims[0])]
class Solution(object):
	def maxProfit(self, K, prices):
		"""
		:type k: int
		:type prices: List[int]
		:rtype: int
		"""
		N = len(prices)
		if not N: return 0

		if K >= N / 2:
			return self.quickSolve(K, prices)

		dp = mdarray(None, N+1, K+1, 2)
		minprice = prices[0]
		for i in xrange(1, N+1):
			minprice = min(minprice, prices[i-1])
			dp[i][0][0] = -minprice
			dp[i][0][1] = 0
			
		for k in xrange(1, K+1):
			dp[1][k][0] = -prices[0]
			dp[1][k][1] = 0
			
		for i in xrange(2, N+1):
			pi = prices[i-1]
			for k in xrange(1, K+1):
				
				dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] - pi)
				dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] + pi)
				# print i, k, dp[i][k][1], dp[i-1][k][1], dp[i-1][k-1][0]
				
		return dp[N][K][1]

	def quickSolve(self, K, prices):
		p0 = prices[0]
		gain = 0
		for i in xrange(1, len(prices)):
			p = prices[i]
			if p > p0:
				gain += p - p0
			p0 = p

		return gain 
