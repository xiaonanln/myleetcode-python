class Solution(object):
	def findUnsortedSubarray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0

		si = 0
		N = len(nums)

		while si < N-1 and nums[si] <= nums[si+1]:
			si += 1

		if si == N-1:
			return 0

		# print 'si', si

		ei = N
		while ei >= 2 and nums[ei-2] <= nums[ei-1]:
			ei -= 1

		# print 'ei', ei, nums[si:ei]
		for i in xrange(si, ei):
			while si > 0 and nums[i] < nums[si-1]:
				si -= 1
			while ei < N and nums[i] > nums[ei]:
				ei += 1

			# print i, nums[i], si, ei, nums[si:ei]
		return ei - si

print Solution().findUnsortedSubarray([])
print Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])

