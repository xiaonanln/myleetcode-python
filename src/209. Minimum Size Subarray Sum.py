class Solution(object):
	def minSubArrayLen(self, s, nums):
		"""
		:type s: int
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0

		i, j = 0, 1
		sum = nums[i]
		N = len(nums)
		while sum < s and j <= N-1:
			sum += nums[j]
			j += 1

		# now sum >= s
		if sum < s:
			return 0

		while sum - nums[i] >= s:
			sum -= nums[i]
			i += 1

		minlen = j - i

		# print minlen, i, j, nums[i:j]
		while j < N:
			sum += nums[j]
			j += 1

			while sum - nums[i] >= s:
				sum -= nums[i]
				i += 1

			minlen = min(minlen, j-i)
			# print minlen, i, j, nums[i:j]

		return minlen


print Solution().minSubArrayLen(11, [1,2,3,4,5])
