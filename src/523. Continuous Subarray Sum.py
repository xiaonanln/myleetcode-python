class Solution(object):
	def checkSubarraySum(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		P = set()
		for n in nums:
			P = {(m+n) % k if k else m+n for m in P}
			if 0 in P:
				return True
			P.add(n)

		return False
