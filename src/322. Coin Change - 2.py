class Solution(object):
	def coinChange(self, coins, amount):
		"""
		:type coins: List[int]
		:type amount: int
		:rtype: int
		"""
		inf = float('inf')
		CN = len(coins)
		dp = [[inf] * (amount+1) for _ in xrange(CN+1)]
		for cn in xrange(0, CN+1):
			dp[cn][0] = 0

		for cn in xrange(1, CN+1):
			cval = coins[cn-1]
			for am in xrange(1, amount+1):
				dp[cn][am] = dp[cn-1][am]
				if am >= cval:
					dp[cn][am] = min(dp[cn][am], 1+dp[cn][am-cval])

		res = dp[CN][amount]
		return res if res != inf else -1

print Solution().coinChange([1, 2, 5], 11)
print Solution().coinChange([2], 3)