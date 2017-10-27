# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
	return version >= 2

class Solution(object):
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		i, j = 1, n
		# print i, j
		while i <= j:
			m = (i + j) // 2
			if isBadVersion(m):
				if m == 1 or not isBadVersion(m - 1):
					return m

				# m is bad, but m-1 is also bad
				j = m - 1
			else:
				# m is good
				i = m + 1

			# print 'loop', i, j
		# print i, j

		assert False

print Solution().firstBadVersion(2)