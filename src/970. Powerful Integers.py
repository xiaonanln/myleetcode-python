class Solution(object):
	def powerfulIntegers(self, x, y, bound):
		"""
		:type x: int
		:type y: int
		:type bound: int
		:rtype: List[int]
		"""
		result = set()
		i = 0
		while x ** i < bound:
			j = 0
			while x ** i + y ** j <= bound:
				# print i, j
				result.add(x ** i + y ** j)
				j += 1
				if y == 1:
					break
			i += 1
			if x == 1:
				break

		return list(result)

# print Solution().powerfulIntegers(3, 5, 15)
print Solution().powerfulIntegers(2, 1, 10)