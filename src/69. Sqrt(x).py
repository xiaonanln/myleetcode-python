class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x <=1: return x 
		i, j = 1, x
		while i < j:
			print i, j
			m = (i+j) // 2
			if m*m == x:
				return m
			elif m*m < x:
				if (m+1)*(m+1) <= x:
					i = m+1
				else:
					return m
			else:
				j = m-1

		return i

print Solution().mySqrt(8)