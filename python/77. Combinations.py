import itertools
class Solution(object):
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		res = []
		for c in itertools.combinations(range(1, n+1), k):
			res.append(c)

		return res

class Solution(object):
	def combine(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		res = []
		sol = []
		used = [False] * (n+1)
		rev = False
		if k >= n // 2:
			k = n - k
			rev = True

		def bt():
			if len(sol) == k:
				if not rev:
					res.append(list(sol))
				else:
					res.append( [num for num in range(1, n+1) if num not in sol] )
				return

			for num in xrange(k - len(sol), n+1):
				if used[num]:
					break

				sol.append(num)
				used[num] = True

				bt()

				used[num] = False
				sol.pop()

		bt()
		return res


for sol in Solution().combine(20, 16):
	print sol