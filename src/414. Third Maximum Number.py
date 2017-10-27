from collections import Counter
class Solution(object):
	def thirdMax(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		C = Counter(nums)
		if len(C) <= 2:
			return max( C.iterkeys() )

		minus_inf = float('-inf')
		a, b, c = minus_inf, minus_inf, minus_inf

		for n, _ in C.iteritems():
			if n > a:
				a, b, c = n, a, b
			elif n > b:
				b, c = n, b
			elif n > c:
				c = n

		return c

print Solution().thirdMax([3, 2, 1])
print Solution().thirdMax([1, 2])
print Solution().thirdMax([2, 2, 3, 1])