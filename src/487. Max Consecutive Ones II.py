class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums: return 0
		contones = []
		numones = 0
		for n in nums:
			if n == 0:
				contones.append(numones)
				numones = 0
			else:
				numones += 1

		contones.append(numones)
		# print contones
		if len(contones) == 1:
			return contones[0]

		return max(contones[i-1] + contones[i] + 1 for i in xrange(1, len(contones)))


print Solution().findMaxConsecutiveOnes([0])
