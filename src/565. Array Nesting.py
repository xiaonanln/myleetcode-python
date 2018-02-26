class Solution(object):
	def arrayNesting(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		maxlen = 1
		for i, n in enumerate(nums):
			if n < 0: # already visited, bypass
				continue
			maxlen = max(maxlen, self.getLenFrom(nums, i) )

	def getLenFrom(self, nums, i):
		seq = [i]

		j = nums[i]
		while nums[j] >= 0:
			print j, nums[j]
			seq.append(j)
			j = nums[j]

		l = -nums[j]
		for i in reversed(seq):
			l += 1
			nums[i] = -l

		return l

print Solution().arrayNesting([5,4,0,3,1,6,2])