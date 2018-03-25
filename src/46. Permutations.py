from itertools import izip
class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		N = len(nums)
		used = [False] * N
		res = []
		sol = []
		def bt():
			if len(sol) == N:
				res.append(list(sol))
				return

			for i, n in enumerate(nums):
				if used[i]: continue
				used[i] = True
				sol.append(n)
				bt()
				sol.pop()
				used[i] = False

		bt()
		return res




print Solution().permute([1,2,3])