
from bisect import bisect_left
class Solution(object):
	def kEmptySlots(self, flowers, k):
		"""
		:type flowers: List[int]
		:type k: int
		:rtype: int
		"""

		S = []
		for ithday, n in enumerate(flowers):
			idx = bisect_left(S, n)
			if idx > 0 and n - S[idx-1] == k+1:
				return ithday + 1
			elif idx < len(S) and S[idx] - n == k+1:
				return ithday + 1
			S.insert(idx, n)

		return -1

print Solution().kEmptySlots([1,3,2], 1)
print Solution().kEmptySlots([1,2,3], 1)
