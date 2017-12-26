import math
class Solution(object):
	def minSteps(self, N):
		"""
		:type n: int
		:rtype: int
		"""
		if N == 1: return 0
		sn = int(math.sqrt(N))
		inf = float('inf')
		res = [inf for i in xrange(N+1)]
		res[1] = 0

		for n in xrange(2, N//2+1):
			res[n] = n
			for v in xrange(n//2, 0, -1):
				if n % v != 0: continue

				res[n] = min(res[n], res[v] + (n // v))
				# print n, v , res[v], res[n]

		res[N] = N
		for v in xrange(N//2, 0, -1):

			if N % v != 0: continue

			res[N] = min(res[N], res[v] + (N // v))
			# print N, v , res[v], res[N]

		return res[N]

print Solution().minSteps(18)