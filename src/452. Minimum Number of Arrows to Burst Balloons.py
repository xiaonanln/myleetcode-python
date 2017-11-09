from operator import itemgetter
class Solution(object):
	def findMinArrowShots(self, points):
		"""
		:type points: List[List[int]]
		:rtype: int
		"""
		points.sort(key=itemgetter(1))
		nclicks = 0
		lastClick = float('-inf')
		for a, b in points:
			if lastClick < a:
				lastClick = b
				nclicks += 1

		return nclicks


print Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])