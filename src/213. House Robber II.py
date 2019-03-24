class Solution(object):
	def rob(self, nums):
		if not nums:
			return 0

		SF, Sf, sF, sf = nums[0], 0, 0, 0
		N = len(nums)
		for i in xrange(1, N):
			n = nums[i]
			SF, Sf, sF, sf = (sF + n if i < N-1 else 0, sf + n, max(sF, SF), max(sf, Sf))

		return max(SF, Sf, sF, sf)




assert Solution().rob([2,3,2]) == 3
assert Solution().rob([1,2,3,1]) == 4