class Solution(object):
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		c = 1
		for i in xrange(len(digits)-1, -1, -1):
			d = digits[i]
			d += 1
			digits[i] = d % 10
			if d >= 10:
				c = 1
			else:
				c = 0
				break

		if c:
			digits[0:0] = [1]
		return digits

print Solution().plusOne([9,9,9])