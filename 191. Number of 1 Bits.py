class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		w = 0
		while n:
			w += 1
			n = n & n - 1
		return w 


