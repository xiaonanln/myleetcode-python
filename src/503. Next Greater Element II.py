class Solution(object):
	def nextGreaterElements(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		stk = []
		L = len(nums)
		res = [-1] * L
		nums = nums + nums[0:L-1]
		for i, n in enumerate(nums):
			while stk and stk[-1][0] < n:
				sn, sidx = stk.pop()
				res[sidx] = n

			if i < L:
				stk.append( (n, i) )

		return res


print Solution().nextGreaterElements([1,2,1])

