class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		N = len(coins)
		M = amount
		dp = [[None] * (M + 1) for _ in xrange(N + 1)]
		
		for i in xrange(N + 1):
			dp[i][0] = 0
		inf = float('inf')
		for j in xrange(1, M + 1):
			dp[0][j] = inf

		for i in xrange(1, N + 1):
			for j in xrange(1, M + 1):
				dp[i][j] = dp[i - 1][j]
				if j >= coins[i-1]:
					dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]]+1)

		return dp[N][M] if dp[N][M] != inf else -1


coins = [1, 2, 5]
amount = 11
print Solution().coinChange(coins, amount)


coins = [2]
amount = 3
print Solution().coinChange(coins, amount)