class Solution(object):
	def combinationSum(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		N = len(candidates)
		dp = [ [None]*(N+1) for _ in xrange(target+1) ]
		for t in xrange(1, target+1):
			dp[t][0] = []

		for i in xrange(N+1):
			dp[0][i] = [ [] ]

		for i in xrange( 1, N+1 ):
			n = candidates[i-1]
			for t in xrange(1, target+1):
				if t >= n:
					dp[t][i] = dp[t][i-1] + [s + [n] for s in dp[t-n][i]]
				else:
					dp[t][i] = dp[t][i - 1]

		return dp[target][N]

print Solution().combinationSum([2, 3, 6, 7], 7)
