
def less(r1, r2):
	d1 = r1[1] - r1[0]
	d2 = r2[1] - r2[0]
	if d1 < d2: return True
	elif d1 == d2:
		return r1[0] < r2[0]
	else:
		return False


class Solution(object):
	def smallestRange(self, nums):
		"""
		:type nums: List[List[int]]
		:rtype: List[int]
		"""
		K = len(nums)
		nums = [(n, j) for j, list in enumerate(nums) for n in list]
		nums.sort()
		knums = [0] * K

		j = 0
		for k in xrange(K):
			while knums[k] == 0:
				n, k_ = nums[j]
				knums[k_] += 1
				j += 1

		i = 0
		k_ = nums[i][1]
		while knums[k_] > 1:
			knums[k_] -= 1
			i += 1
			k_ = nums[i][1]

		smr = [nums[i][0], nums[j-1][0]]
		# print knums, i, j, smr
		while j < len(nums):
			n, k_ = nums[j]
			knums[k_] += 1
			j += 1
			# print 'add', n, k_, [nums[i][0], nums[j-1][0]], knums

			k_ = nums[i][1]
			while knums[k_] > 1:
				knums[k_] -= 1
				i += 1
				k_ = nums[i][1]
				# print 'remove', nums[i-1], [nums[i][0], nums[j-1][0]], knums


			r = [nums[i][0], nums[j-1][0]]
			# print i, j, smr, r, knums
			if less(r, smr):
				smr = r

		return smr






print Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])
