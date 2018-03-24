from math import sqrt
class Solution(object):
	def getFactors(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		if n == 1:
			return []

		res = []
		sol = []
		def bt(num, minfactor, ):
			if num == 1:
				res.append(list(sol))
				return

			for f in xrange(minfactor, int(sqrt( num ))+1):
				if num % f == 0:
					# print num, f
					sol.append(f)
					bt(num//f, f)
					sol.pop()

			if sol:
				sol.append(num)
				bt(1, num)
				sol.pop()

		bt(n, 2)
		return res


print Solution().getFactors(1)
print Solution().getFactors(37)
print Solution().getFactors(12)
print Solution().getFactors(32)
