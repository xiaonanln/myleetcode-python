class Solution(object):
	def maxSumOfThreeSubarrays(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""

		N = len(nums)

		s = sum(nums[i] for i in xrange(k))
		dp1 = [None] * (N+1)
		maxS = dp1[k] = (s, 0)
		for i in xrange(k+1, N+1):
			# add nums[k] and remove nums[i-k]
			s = s + nums[i-1] - nums[i-1-k]
			if s > maxS[0]:
				maxS = (s, i-k)
			dp1[i] = maxS

		s = sum(nums[i] for i in xrange(k, k*2))
		dp2 = [None] * (N+1)
		maxS = dp2[k*2] = (s+dp1[k][0], 0, k)

		for i in xrange(k*2 + 1, N + 1):
			# add nums[k] and remove nums[i-k]
			s = s + nums[i - 1] - nums[i - 1 - k]
			if s + dp1[i-k][0] > maxS[0]:
				maxS = (s + dp1[i-k][0], dp1[i-k][1], i - k)
			dp2[i] = maxS

		s = sum(nums[i] for i in xrange(k*2, k*3))
		maxS = s+dp2[k*2][0]
		res = [0, k, k*2]

		for i in xrange(k*3 + 1, N + 1):
			# add nums[k] and remove nums[i-k]
			s = s + nums[i - 1] - nums[i - 1 - k]
			if s + dp2[i-k][0] > maxS:
				maxS = s + dp2[i-k][0]
				res = [dp2[i-k][1], dp2[i-k][2], i - k]

		return res

print Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)

