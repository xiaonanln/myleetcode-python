class Solution(object):
	def maxCoins(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		N = len(nums)
		nums.append(1)
		dp = [[0] * (N+1) for _ in xrange(N+1)]

		for l in xrange(1, N+1): # l = 1 ~ N
			for i in xrange(0, N-l+1):
				j = i + l # j = i ~ N it is always better to use j index to indicate nums from i to j-122
				for k in xrange(i, j): # k = i ~ j
					dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j])

		return dp[0][N]


print Solution().maxCoins([3, 1, 5, 8])
