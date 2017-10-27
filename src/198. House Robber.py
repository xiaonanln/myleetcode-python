class Solution(object):
	def rob(self, nums):
		a, b = 0, 0
		for n in nums: a, b = max(b, a), a + n
		return max(b, a)

print Solution().rob([1,1])