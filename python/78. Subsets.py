class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		N = len(nums)
		choose = [0] * N
		res = []
		def bt(n):
			if n == N:
				res.append( [nums[i] for i, c in enumerate(choose) if c] )
				return

			choose[n] = 0
			bt(n+1)

			choose[n] = 1
			bt(n+1)

		bt(0)
		return res

class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		sets = [ [] ]
		for n in nums:
			newsets = [s + [n] for s in sets]
			sets += newsets
		return sets

print Solution().subsets([1,2,3])