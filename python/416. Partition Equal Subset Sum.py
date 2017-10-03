class SolutionMemo(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		N = len(nums)
		maxsum = [0] * (N+1)
		totalSum = 0
		for i, n in enumerate(nums):
			maxsum[i+1] = maxsum[i] + n
			totalSum += n

		# print maxsum, totalSum
		if totalSum % 2 != 0:
			return False

		findSum = totalSum / 2

		memo = {}

		def canPartitionHelper(n, sum):
			# print 'canPartitionHelper', n, sum
			if sum == 0: return True
			if sum < 0: return False
			if maxsum[n] < sum: return False

			key = (n, sum)
			if key in memo:
				return memo[key]

			can = canPartitionHelper(n-1, sum)
			if not can and nums[n-1] <= sum:
				can = canPartitionHelper(n-1, sum-nums[n-1])

			memo[key] = can
			return can

		return canPartitionHelper( N, findSum )

class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		N = len(nums)
		maxsum = [0] * (N+1)
		totalSum = 0
		for i, n in enumerate(nums):
			maxsum[i+1] = maxsum[i] + n
			totalSum += n

		if totalSum % 2 != 0:
			return False

		findSum = totalSum / 2
		dp = [ [False] * (findSum+1) for _ in xrange(N+1) ] # dp[n][s] == first n number can sum to s ?
		for n in xrange(N+1):
			dp[n][0] = True

		for n in xrange(N+1):
			ms =  maxsum[n]
			nn = nums[n-1]
			for s in xrange(1, min(findSum, ms)+1):
				dp[n][s] = dp[n-1][s] or (s >= nn and dp[n-1][s-nn])

		return dp[N][findSum]

print Solution().canPartition([1, 5, 11, 5])
print Solution().canPartition([1, 2, 3, 5])