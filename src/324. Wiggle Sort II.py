class Solution(object):
	def wiggleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		snums = sorted(nums)
		i = 0
		j = (len(nums)+1) // 2
		w = 0
		N = len(nums)
		while j < N:
			nums[w] = snums[i]
			nums[w+1] = snums[j]
			i += 1
			j += 1
			w += 2
		#
		# print i, j, w , (len(nums)+1) //2
		if i < (len(nums)+1)//2:
			nums[w] = snums[i]




nums = [1,3,2,2,1,1,3]
Solution().wiggleSort(nums)
print nums

# nums = [1, 5, 1, 1, 6, 4]
# Solution().wiggleSort(nums)
# print nums
#
# nums = [1, 5, 1, 1, 6, 4, 3]
# Solution().wiggleSort(nums)
# print nums
#
#
# nums = [1, 3, 2, 2, 3, 1]
# Solution().wiggleSort(nums)
# print nums