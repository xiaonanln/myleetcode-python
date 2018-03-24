
class Solution(object):
	def judgePoint24(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		nums = [float(n) for n in nums]
		def bt():
			# print 'bt', nums
			if len(nums) == 1:
				return abs(nums[0] - 24) < 0.000001

			N = len(nums)
			for i in xrange(N-1):
				n1 = nums[i]
				for j in xrange(i+1, N):
					# choose i and j
					n2 = nums[j]
					orig_ij = n1, n2
					# remove the value j
					nums.pop(j)
					for v in ((n1+n2), (n1-n2), (n2-n1), (n1*n2), ):
						nums[i] = v
						if bt(): return True

					if n2 != 0:
						nums[i] = n1/n2
						if bt(): return True

					if n1 != 0:
						nums[i] = n2/n1
						if bt(): return True

					# restore nums
					nums[i] = n1
					nums.insert(j, n2)

			return False

		return bt()

print Solution().judgePoint24([1,1,7,7])
# print Solution().judgePoint24([1, 2, 1, 2])










