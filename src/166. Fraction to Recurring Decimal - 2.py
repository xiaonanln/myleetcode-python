class Solution(object):
	def fractionToDecimal(self, numerator, denominator):
		"""
		:type numerator: int
		:type denominator: int
		:rtype: str
		"""
		if numerator == 0: return '0'
		if numerator < 0 and denominator < 0:
			return self.fractionToDecimal(-numerator, -denominator)
		elif numerator < 0:
			return '-' + self.fractionToDecimal(-numerator, denominator)
		elif denominator < 0:
			return '-' + self.fractionToDecimal(numerator, -denominator)

		d, numerator = divmod(numerator, denominator)
		if numerator == 0:
			return str(d)

		s = str(d) + '.'
		nums = {}
		numerator *= 10
		while numerator:
			if numerator in nums:
				# print nums, numerator
				return s[:nums[numerator]] + '(' + s[nums[numerator]:] + ')'

			nums[numerator] = len(s)
			# print nums, numerator, denominator
			d, numerator = divmod(numerator, denominator)
			s = s + str(d)
			numerator *= 10

		return s




# print Solution().fractionToDecimal(1, 2)
# print Solution().fractionToDecimal(2, 1)
print Solution().fractionToDecimal(-22, -2)
