class Solution(object):
	def maxRotateFunction(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		N = len(A)
		S = sum(A)
		F = sum(i * a for i, a in enumerate(A))
		maxF = F
		for r in xrange(1, N): # rotate in 1 ~ N-1
			si = N - r
			F = F + S - A[si] * N
			maxF = max(maxF, F)

		return maxF


print Solution().maxRotateFunction([4, 3, 2, 6])