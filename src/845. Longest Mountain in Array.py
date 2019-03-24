class Solution(object):
	def longestMountain(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		start, end = None, None
		N = len(A)
		lm = 0
		for i in xrange(N-1):
			n0, n1 = A[i], A[i+1]
			assert (start is None and end is None) or (start is not None and end is None) or (start is not None and end is not None)
			if n0 < n1:
				if end is not None:
					lm = max(lm, end - start + 1)
					start, end = None, None

				if start is None:
					start = i

			elif n0 == n1:
				if end is not None:
					lm = max(lm, end - start + 1)
					start, end = None, None

				if start is not None:
					start, end = None, None

			else: # n0 > n1
				if end is not None:
					assert end == i
					end = i+1
				elif start is not None:
					assert end is None
					end = i+1

		if end:
			lm = max(lm, end - start + 1)

		return lm