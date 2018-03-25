class Solution(object):
	def increasingTriplet(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		a, b = float('inf'), float('inf')
		for n in nums:
			if n < a: a = n
			elif n > a and n < b:
				b = n
			elif n > b:
				return True

		return False


print Solution().increasingTriplet([1, 2, 3, 4, 5])
print Solution().increasingTriplet([5,4,3,2,1])