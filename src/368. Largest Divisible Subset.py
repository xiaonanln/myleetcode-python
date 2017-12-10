class Solution(object):
	def largestDivisibleSubset(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums: return []
		nums.sort()
		N = len(nums)
		ldss = [1] * N # largest divisible subset size
		prev = [None] * N  # previous
		for i, num in enumerate(nums):
			for j in xrange(i-1, -1, -1): # j = i-1 to 0
				if num % nums[j] == 0 and ldss[j] + 1 > ldss[i]:
					ldss[i] = ldss[j] + 1
					prev[i] = j

		maxsize, maxi = 1, 0
		for i, size in enumerate(ldss):
			if size > maxsize:
				maxsize = size
				maxi = i


		ss = []
		while maxi is not None:
			ss.append( nums[maxi] )
			maxi = prev[maxi]

		return ss

print Solution().largestDivisibleSubset([1,2,3])
print Solution().largestDivisibleSubset([1,2,4,8])
print Solution().largestDivisibleSubset([1,2,4,7, 8])