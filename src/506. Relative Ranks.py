class Solution(object):
	def findRelativeRanks(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		nums = [(n, i) for i, n in enumerate(nums)]
		nums.sort(reverse=True)
		# print nums
		res = [None] * len(nums)
		for rank, (n, i) in enumerate(nums):
			if rank <= 2:
				res[i] = ("Gold Medal", "Silver Medal", "Bronze Medal")[rank]
			else:
				res[i] = str(rank+1)

		return res





print Solution().findRelativeRanks([5, 4, 3, 2, 1])