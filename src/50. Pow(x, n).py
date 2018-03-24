class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		if n == 0:
			return 1
		elif n == 1:
			return x

		if n % 2 == 0:
			v = pow(x, n//2)
			return v*v
		else:
			v = pow(x, n // 2)
			return x*v*v