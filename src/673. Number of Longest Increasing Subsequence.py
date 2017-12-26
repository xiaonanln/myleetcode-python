class Solution(object):
	def findNumberOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		N = len(nums)
		if N == 0:
			return 0

		longest = [ None for _ in nums ]

		for i in xrange(N):
			longest[i] = [1, 1]

			for j in xrange(i-1, -1, -1):
				if nums[j] < nums[i]:
					if longest[j][0] >= longest[i][0]:
						longest[i] = [longest[j][0] + 1, longest[j][1]]
					elif longest[j][0] == longest[i][0] - 1:
						longest[i][1] += longest[j][1]

			# print longest

		longestLen = max(_[0] for _ in longest)
		# print longestLen, longest
		return sum( _[1] for _ in longest if _[0] == longestLen )

print Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3])
