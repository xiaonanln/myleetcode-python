from math import sqrt
class Solution(object):
	def constructRectangle(self, area):
		"""
		:type area: int
		:rtype: List[int]
		"""
		d = int(sqrt(area))
		for v in xrange(d, 0, -1):
			if area % v == 0:
				return [area//v, v]

print Solution().constructRectangle(4)
print Solution().constructRectangle(6)
