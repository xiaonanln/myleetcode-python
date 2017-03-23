class Solution(object):
	def wiggleMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) <= 1: return len(nums)
		elif len(nums) == 2: 
			return 2 if nums[0] != nums[1] else 1

		i = 0
		j = 1
		while j < len(nums) and nums[j] == nums[i]:
			j += 1 # find j that nums[i] != nums[j]

		if j == len(nums): return 1

		# now i != j 
		dir = nums[j] - nums[i] # find first dir
		if dir > 0:
			while j+1 < len(nums) and nums[j+1] >= nums[j]:
				j += 1
		else:
			while j+1 < len(nums) and nums[j+1] <= nums[j]:
				j += 1

		numWiggle = 2
		k = j + 1
		while k < len(nums):
			if dir > 0:
				while k+1 < len(nums) and nums[k+1] <= nums[k]:
					k += 1
			else:
				while k+1 < len(nums) and nums[k+1] >= nums[k]:
					k += 1

			numWiggle += 1
			# print i, j, k, dir, numWiggle, nums[:k+1]
			i, j, k = j, k, k+1
			dir = -dir

		return numWiggle


print Solution().wiggleMaxLength([1,7,4,9,2,5])
print Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])
print Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9])
