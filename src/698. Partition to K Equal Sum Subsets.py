class Solution(object):
	def canPartitionKSubsets(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		if not nums:
			return True

		nums.sort()
		S = sum(nums)
		if S % k != 0:
			return False

		s = S // k
		sums = [0] * k
		L = len(nums)
		if max(nums) > s:
			return False

		def bt(i):
			# print i, sums
			if i == L:
				return True

			n = nums[i]
			for j, _s in enumerate(sums):
				if _s + n > s or 0< s - (_s + n) < n :
					continue

				sums[j] += n
				if bt(i+1):
					return True
				sums[j] -= n

			return False

		return bt(0)



print Solution().canPartitionKSubsets([730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908], 4)