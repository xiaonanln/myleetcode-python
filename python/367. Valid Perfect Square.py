class Solution(object):
	def isPerfectSquare(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		l, r = 1, num

		while l <= r:

			m = (l + r) // 2
			mm = m * m
			# print l, r, m, mm, '->',
			if num < mm:
				r = m - 1
			elif num > mm:
				l = m + 1
			else:
				return True

			# print l, r, m, mm

		return False

# print Solution().isPerfectSquare(1)
print Solution().isPerfectSquare(2)
# print Solution().isPerfectSquare(4)
# print Solution().isPerfectSquare(16)